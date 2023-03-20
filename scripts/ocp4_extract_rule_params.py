#!/usr/bin/python3
"""
Takes given DataStream and produces rules+parms json file.

Author: Lou DeGenaro <degenaro@us.ibm.com>
"""

import argparse
import json
import logging
import pathlib
from typing import Dict, List, Union

import defusedxml.ElementTree as ElementTree

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname).1s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

prefix = 'xccdf_org.ssgproject'
prefix_value = f'{prefix}.content_value_'
prefix_rule = f'{prefix}.content_rule_'

ds_version = '1.2'
ns_key = f'xccdf-{ds_version}'
ns_val = f'http://checklists.nist.gov/xccdf/{ds_version}'
ns = {f'{ns_key}': f'{ns_val}'}

in_filename = f'ssg-ocp4-ds-{ds_version}.xml'
out_filename = 'rule2var.json'


class ParmInfo():
    """Class ParmInfo."""

    def __init__(self, id_: str, type_: str):
        """Initialize."""
        self.id = id_
        self.type = type_
        self.value = None
        self.choices = {}
        self.title = None
        self.description = None

    def add_value(self, value: str):
        """Add the chosen value."""
        self.value = value

    def add_choice(self, name: str, value: str):
        """Add a choice name:value pair."""
        if value:
            self.choices[name] = value

    def add_title(self, value: str):
        """Add the title."""
        self.title = value

    def add_description(self, value: str):
        """Add the description."""
        self.description = value

    def get_id(self) -> str:
        """Get the id."""
        return self.id

    def get_type(self) -> str:
        """Get the type."""
        return self.type

    def get_value(self) -> str:
        """Get the chosen value."""
        return self.value

    def get_choices(self) -> Dict:
        """Get the choices named:value pairs."""
        return self.choices

    def get_title(self) -> str:
        """Get the chosen title."""
        return self.title

    def get_description(self) -> str:
        """Get the chosen description."""
        return self.description


class RuleInfo():
    """Class RuleInfo."""

    def __init__(self):
        """Initialize."""
        self.exports = []
        self.fixes = []

    def add_export(self, value: str):
        """Add a check-export."""
        if value:
            self.exports += [value]

    def add_fix(self, value: str):
        """Add a fix."""
        if value:
            self.fixes += [value]

    def get_exports(self) -> List[str]:
        """Get the exports."""
        return self.exports

    def get_fixes(self) -> List[str]:
        """Get the fixes."""
        return self.fixes


class Extractor():
    """Class Extractor."""

    def normalize_rule_name(self, r_name: str) -> str:
        """Normalize rule name."""
        rule = r_name
        if r_name.startswith(prefix_rule):
            rule = r_name.replace(prefix_rule, '')
        return rule

    def run(self):
        """Run."""
        rule2var = {}
        # parse args
        args = self.parse_args()
        # xml element tree
        root_element = ElementTree.parse(args.input, forbid_dtd=True)
        # create parameter map
        parameter_map = self.get_parameter_map(root_element, ns)
        # create rule map
        rule_map = self.get_rule_map(root_element, ns)
        # process each parameter -> rule pair
        for p_key in parameter_map:
            r_name = self.get_rule(rule_map, p_key)
            # skip parameter if no rule associated
            if not r_name:
                text = f'no rule found for parameter {p_key}'
                logger.warning(text)
            # add parameter -> rule entry
            else:
                parm_info = parameter_map[p_key]
                options = {}
                options['default'] = parm_info.get_value()
                choices = parm_info.get_choices()
                for c_key in choices.keys():
                    options[c_key] = choices[c_key]
                entry = {}
                entry['id'] = parm_info.get_id()
                entry['type'] = parm_info.get_type()
                entry['title'] = parm_info.get_title()
                entry['description'] = parm_info.get_description()
                entry['options'] = options
                rule = self.normalize_rule_name(r_name)
                rule2var[rule] = entry
        # create/re-write json file
        pout = pathlib.Path(f'{args.output}')
        pout.mkdir(parents=True, exist_ok=True)
        pout = pout / out_filename
        with open(pout, 'w') as ofile:
            json_object = json.dumps(rule2var, indent=4)
            ofile.write(json_object)
            print(f'output: {pout}')

    def get_rule(self, rule_map: Dict, p_key: str) -> Union[str, None]:
        """Get rule."""
        rval = None
        for r_key in rule_map.keys():
            rule_info = rule_map[r_key]
            exports = rule_info.get_exports()
            for export in exports:
                if export == p_key:
                    return r_key
            fixes = rule_info.get_fixes()
            for fix in fixes:
                if f'{prefix_value}{fix}' == p_key:
                    return r_key
        return rval

    def parse_args(self):
        """Parse args."""
        description = 'Extract rules and parameters from datastream xml file into json file'
        p = argparse.ArgumentParser(description=description)
        help_i = f'input file xml datastream, e.g. {in_filename}'
        help_o = 'output directory'
        p.add_argument('-i', '--input', action='store', required=True, help=help_i)
        p.add_argument('-o', '--output', action='store', required=True, help=help_o)
        return p.parse_args()

    def get_parameter_map(self, tree: ElementTree, ns: Dict) -> Dict:
        """Get parameter map: parameter name to selected + choices list."""
        map_ = {}
        items = tree.findall(f'.//{ns_key}:Value', ns)
        for item in items:
            parameter_info = self.get_parameter_info(item, ns)
            if parameter_info:
                id_ = item.get('id')
                map_[id_] = parameter_info
        return map_

    def get_parameter_info(self, tree: ElementTree, ns: Dict) -> ParmInfo:
        """Get parameter info comprising selected and choices list."""
        id_ = tree.get('id').replace(prefix_value, '')
        type_ = tree.get('type')
        parm_info = ParmInfo(id_, type_)
        items = tree.findall(f'.//{ns_key}:value', ns)
        for item in items:
            value = item.text
            name = item.get('selector')
            if name:
                parm_info.add_choice(name, value)
            else:
                parm_info.add_value(value)
        item = tree.find(f'.//{ns_key}:title', ns)
        value = item.text
        parm_info.add_title(value)
        item = tree.find(f'.//{ns_key}:description', ns)
        value = item.text
        parm_info.add_description(value)
        # empty?
        selected = parm_info.get_value()
        choices = parm_info.get_choices()
        if not selected and not choices:
            parm_info = None
        return parm_info

    def get_rule_map(self, tree: ElementTree, ns: Dict) -> Dict:
        """Get rule map: rule name to parameter name + parameter short-name list."""
        map_ = {}
        items = tree.findall(f'.//{ns_key}:Rule', ns)
        for item in items:
            rule_info = self.get_rule_info(item, ns)
            if rule_info:
                id_ = item.get('id')
                map_[id_] = rule_info
        return map_

    def get_rule_info(self, tree: ElementTree, ns: Dict) -> RuleInfo:
        """Get rule info comprising export and fix list."""
        rule_info = RuleInfo()
        # exports
        exports = tree.findall(f'.//{ns_key}:check-export', ns)
        for export in exports:
            value = export.get('value-id')
            if value:
                rule_info.add_export(value)
        # fixes
        fixes = tree.findall(f'.//{ns_key}:fix', ns)
        start = '{{'
        end = '}}'
        for fix in fixes:
            lines = fix.text.split('\n')
            for line in lines:
                try:
                    value = line.split(start)[1].split(end)[0]
                    value = value.replace('.', '')
                    if value.startswith('var_'):
                        rule_info.add_fix(value)
                except IndexError:
                    text = f'Index Error processing line {line}'
                    logger.debug(text)
        # empty?
        exports = rule_info.get_exports()
        fixes = rule_info.get_fixes()
        if not exports and not fixes:
            rule_info = None
        return rule_info


#####


def main():
    """Mainline."""
    extractor = Extractor()
    extractor.run()


if __name__ == '__main__':
    main()
