# command

#### ocp4_cis_profile_to_csv.py

##### Purpose: 

create ocp4.csv file from CIS Benchmarks profile(s) + OSCAL catalog(s)

##### Requirements: 

- trestle

##### Sample invocation:

python scripts/ocp4_cis_profile_to_csv.py --input data/cis-benchmarks/cis-node.profile profiles/OCP4_CIS_NODE/profile.json "OCP4 CIS Node Profile" --input data/cis-benchmarks/cis.profile profiles/OCP4_CIS/profile.json "OCP4 CIS Profile" --check-prefix xccdf_org.ssgproject.content_rule_ --catalog catalogs/ocp4-cis/catalog.json --rule-to-parameters-map data/rule2var.json --output data/
