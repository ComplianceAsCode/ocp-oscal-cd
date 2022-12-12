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
"""Create ocp4.csv from CIS benchmarks file(s)."""
import argparse
import datetime
import logging
import pathlib

from utils.cis_utils import CisOscalCatalogHelper, CisProfileHelper
from utils.csv_utils import CsvHelper

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname).1s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
logger = logging.getLogger(__name__)

timestamp = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()

column_names = [
    'Rule_Id',
    'Rule_Description',
    'Profile_Reference_URL',
    'Profile_Description',
    'Component_Type',
    'Control_Mappings',
    'Resource',
    'Parameter_Id',
    'Parameter_Description',
    'Parameter_Default_Value',
    'Parameter_Value_Alternatives'
]

default_component_type = 'Service'
default_resource = 'OSCO'
default_rule_prefix = ''
default_rule_prefix_help = 'None'


class Mainline:
    """Main."""

    def __init__(self):
        """Initialize."""
        self.profile_helpers = []
        self.catalog_helpers = []

    def parse(self) -> dict:
        """Parse."""
        parser = argparse.ArgumentParser(description='Create ocp4.csv from CIS Benchmarks')
        parser.add_argument(
            '--catalog',
            type=str,
            required=False,
            action='append',
            help='catalog file; can be specified more than once; employed for validation'
        )
        ht1 = 'CIS Benchmark 3-tuple comprising:'
        ht2 = '1=file 2=URL 3=description;'
        ht3 = 'at least one input 3-tuple is required;'
        ht4 = 'can be specified more than once'
        parser.add_argument(
            '--input',
            type=str,
            required=True,
            action='append',
            nargs=3,
            metavar=('FILE', 'URL', 'DESCRIPTION'),
            help=f'{ht1} {ht2} {ht3} {ht4}'
        )
        parser.add_argument('--output', type=str, required=True, help='output folder for generated ocp4.csv')
        # optional
        parser.add_argument(
            '--component-type',
            type=str,
            required=False,
            default=f'{default_component_type}',
            help=f'component type, default = {default_component_type}'
        )
        parser.add_argument(
            '--resource',
            type=str,
            required=False,
            default=f'{default_resource}',
            help=f'resource, default = {default_resource}'
        )
        parser.add_argument(
            '--rule-prefix',
            type=str,
            required=False,
            default=f'{default_rule_prefix}',
            help=f'rule-prefix, default = {default_rule_prefix_help}'
        )
        args = parser.parse_args()
        return args

    def _is_included(self, control_id: str) -> bool:
        rval = False
        for catalog_helper in self.catalog_helpers:
            if catalog_helper.is_present(control_id):
                rval = True
                break
        return rval

    def run(self) -> None:
        """Run."""
        args = self.parse()
        # minimally validate input file(s)
        for input_ in args.input:
            file_ = input_[0]
            url_ = input_[1]
            desc_ = input_[2]
            ipath = pathlib.Path(file_)
            if not ipath.is_file():
                text = f'input file "{file_}" not found'
                raise Exception(text)
            self.profile_helpers.append(CisProfileHelper(file_, url_, desc_))
        # minimally validate catalog file(s)
        for catalog in args.catalog:
            ipath = pathlib.Path(catalog)
            if not ipath.is_file():
                text = f'catalog file "{catalog}" not found'
                raise Exception(text)
            self.catalog_helpers.append(CisOscalCatalogHelper(ipath))
        # prepare output
        opath = pathlib.Path(args.output)
        if not opath.is_dir():
            opath.mkdir(parents=True, exist_ok=True)
        # process
        rows = []
        for profile_helper in self.profile_helpers:
            for cis_node in profile_helper.node_generator():
                if cis_node.rules is not None:
                    control_id = f'CIS-{cis_node.name}'
                    if not self._is_included(control_id):
                        logger.info(f'skip: {control_id}')
                        continue
                    for rule in cis_node.rules:
                        rule_id = f'{args.rule_prefix}{rule.strip()}'
                        row = [
                            f'{rule_id}',
                            f'{cis_node.description}',
                            f'{profile_helper.get_url()}',
                            f'{profile_helper.get_description()}',
                            f'{args.component_type}',
                            f'{control_id}',
                            f'{args.resource}',
                            '',
                            '',
                            '',
                            ''
                        ]
                        rows.append(row)
        # write csv
        self.csv_helper = CsvHelper(opath, 'ocp4.csv')
        self.csv_helper.write(column_names, rows)


def main():
    """Create OSCAL profile.json from spread sheet."""
    mainline = Mainline()
    mainline.run()


if __name__ == '__main__':
    main()
