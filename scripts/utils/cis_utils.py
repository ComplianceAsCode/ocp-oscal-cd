# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2022 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""CIS utils."""
import logging
import pathlib
from typing import List, Optional, ValuesView

from pydantic import BaseModel, Field

from trestle.common import const
from trestle.oscal.catalog import Catalog
from trestle.oscal.catalog import Control
from trestle.oscal.catalog import Group

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname).1s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
logger = logging.getLogger(__name__)


class CisNode(BaseModel):
    """Representation of CIS profile entry."""

    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    rules: List[str] = Field(None)

    def _depth(self):
        """Depth."""
        lhs = self.name.split()[0]
        dots = lhs.split('.')
        depth = len(dots)
        return depth


class CisProfileHelper:
    """CIS Profile Helper common functions and assistance."""

    def __init__(self, file_: str, url_: str, description_: str) -> None:
        """Initialize."""
        self._file = file_
        self._url = url_
        self._description = description_
        self._ipath = pathlib.Path(file_)
        self._node_map = {}
        lines = self._get_content(self._ipath)
        self._parse(lines)

    def _parse(self, lines: List[str]) -> None:
        """Parse lines to build data structure."""
        cis_node = None
        for line in lines:
            if line.startswith('    - '):
                rule = line.split('    - ')[1]
                if cis_node.rules is None:
                    cis_node.rules = []
                cis_node.rules.append(rule)
            line = line.strip()
            if line.startswith('title: ') and "'" in line:
                self._title = line.split("'")[1]
                continue
            line_parts = line.split(None, 2)
            # must be 3 parts exactly
            if len(line_parts) < 3:
                continue
            # normalized name and description
            name = line_parts[1].rstrip('.')
            description = line_parts[2]
            # name must be numbers and decimal points
            if not set(name) <= set('0123456789.'):
                continue
            # derive desired sortable key from name
            key = self._get_key(name)
            cis_node = CisNode(name=name, description=description)
            self._node_map[key] = cis_node

    def _get_content(self, fp: pathlib.Path) -> List[str]:
        """Fetch content from file."""
        content = None
        try:
            f = fp.open('r', encoding=const.FILE_ENCODING)
            content = f.readlines()
            f.close()
            return content
        except Exception as e:
            logger.warning(f'unable to process {fp.name}')
            raise e

    def _get_key(self, name: str) -> (int, int, int):
        """Convert name to desired sortable key."""
        parts = name.split('.')
        if len(parts) == 1:
            key = (int(parts[0]), 0, 0)
        elif len(parts) == 2:
            key = (int(parts[0]), int(parts[1]), 0)
        elif len(parts) == 3:
            key = (int(parts[0]), int(parts[1]), int(parts[2]))
        else:
            text = f'Unexpected value: {name}'
            raise RuntimeError(text)
        return key

    def _get_root_nodes(self) -> ValuesView[CisNode]:
        """Get root nodes."""
        root_nodes = {}
        for node in self._node_map.values():
            if len(node.name) == 1:
                root_nodes[node.name] = node
        return root_nodes.values()

    def root_node_generator(self) -> CisNode:
        """Root node generator."""
        for root_node in self._get_root_nodes():
            yield root_node

    def node_generator(self) -> CisNode:
        """Node generator."""
        for node in self._node_map.values():
            yield node

    def get_url(self):
        """Get URL."""
        return self._url

    def get_description(self):
        """Get description."""
        return self._description


class CisOscalCatalogHelper:
    """CIS OSCAL Catalog Helper common functions and assistance."""

    def __init__(self, catalog_file: str) -> None:
        """Initialize."""
        # arrays
        self._control_ids_list = []
        # init
        self._catalog_name = catalog_file
        cpath = pathlib.Path(catalog_file)
        if not cpath.is_file():
            text = f'input file "{cpath}" not found'
            raise Exception(text)
        catalog = Catalog.oscal_read(cpath)
        control_ids_list = []
        self._ingest_catalog_groups(catalog.groups, control_ids_list)
        self._ingest_catalog_controls(catalog.groups, control_ids_list, None, None)
        self._control_ids_list = control_ids_list
        logger.debug(f'{control_ids_list}')

    def _ingest_catalog_groups(self, groups: List[Group], control_ids: List[str]) -> None:
        if groups:
            for group in groups:
                self._ingest_catalog_groups(group.groups, control_ids)
                self._ingest_catalog_controls(group.controls, control_ids, group, None)

    def _ingest_catalog_controls(
        self, controls: List[Control], control_ids: List[str], group: Group, parent_control: Control
    ) -> None:
        if controls:
            for control in controls:
                control_ids.append(control.id)
                self._ingest_catalog_controls(control.controls, control_ids, group, control)

    def is_present(self, control_id) -> bool:
        """Check if catalog contains specified control id."""
        return control_id in self._control_ids_list
