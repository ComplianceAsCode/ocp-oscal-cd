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
"""Csv utils."""
import csv
import pathlib
from typing import List


class CsvHelper:
    """CIS Profile Helper common functions and assistance."""

    def __init__(self, ipath: pathlib.Path, fname: str) -> None:
        """Initialize."""
        self._ipath = ipath / fname

    def write(self, columns: List[str], rows: List[List[str]]):
        """Write the output file."""
        # process csv
        with open(self._ipath, 'wt', encoding='utf-8') as output:
            csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(columns)
            for row in rows:
                csv_writer.writerow(row)
