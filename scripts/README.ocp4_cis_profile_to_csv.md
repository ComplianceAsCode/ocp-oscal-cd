# Procedure to create ocp4.csv

##### Purpose: 

create ocp4.csv file from:

- CIS Benchmarks profile(s)
- OSCAL catalog(s)
- OCP4 extracted parameters

##### Requirements: 

- trestle
- download of ComplianceAsCode ocp-oscal-cd (this repo)
- download of ComplianceAsCode content

##### 1. install trestle

```
degenaro:~$ python -m venv venv.ocp4
degenaro:~$ source venv.ocp4/bin/activate
(venv.ocp4) degenaro:~$ pip install pip install compliance-trestle
```

##### 2. download repos

```
(venv.ocp4) degenaro:~$ cd /tmp
(venv.ocp4) degenaro:tmp$ mkdir cac
(venv.ocp4) degenaro:tmp$ cd cac
(venv.ocp4) degenaro:cac$ git clone https://github.com/ComplianceAsCode/ocp-oscal-cd.git
(venv.ocp4) degenaro:cac$ git clone https://github.com/ComplianceAsCode/content.git
```

##### 3. build ComplianceAsCodeContent for ocp4

```
(venv.ocp4) degenaro:cac$ cd content
(venv.ocp4) degenaro:content$ ./build_product -d ocp4
```

##### 4. extract ocp4 parameter info

```
(venv.ocp4) degenaro:content$ cd ../ocp-oscal-cd
degenaro:ocp-oscal-cd$ python scripts/ocp4_extract_rule_params.py -i ../content/build/ssg-ocp4-ds-1.2.xml -o data

```

Note: a warning is given for those parameters not linked to any rule

<details>
<summary>console</summary>

03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_hypershift_cluster  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_ocp_version_api_path  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_ocp_version_yaml_path  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_apiserver_audit_log_maxsize  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_apiserver_encryption_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_apiserver_encryption_path  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_apiserver_config  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_apiserver_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_apiserver_namespace  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_kube_apiserver_config  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_kube_apiserver_config_data_name  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_openshift_kube_apiserver_namespace  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_config_data_name  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_config_filepath  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_port_zero_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_rotate_kubelet_server_certs_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_secure_port_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_service_account_ca_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_service_account_private_key_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_controller_manager_use_service_account_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_etcd_argument_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_etcd_filepath  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_kube_authorization_mode  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_sccs_with_allowed_capabilities_regex  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_scheduler_argument_filter  
03/10/2023 10:24:06 W no rule found for parameter xccdf_org.ssgproject.content_value_var_scheduler_filepath  

</details>

##### 6. create ocp4.csv

```
(venv.ocp4) degenaro:ocp-oscal-cd$ python scripts/ocp4_cis_profile_to_csv.py --input data/cis-benchmarks/cis-node.profile profiles/OCP4_CIS_NODE/profile.json "OCP4 CIS Node Profile" --input data/cis-benchmarks/cis.profile profiles/OCP4_CIS/profile.json "OCP4 CIS Profile" --check-prefix xccdf_org.ssgproject.content_rule_ --catalog catalogs/ocp4-cis/catalog.json --rule-to-parameters-map data/rule2var.json --output data/
```

Note: file data/ocp4.csv is created

