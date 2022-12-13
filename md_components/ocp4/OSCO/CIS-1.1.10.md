---
x-trestle-comp-def-rules:
  - name: file_owner_cni_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_cni_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_multus_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_multus_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ip_allocations
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ip_allocations
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_openshift_sdn_cniserver_config
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_openshift_sdn_cniserver_config
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovs_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovs_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovs_conf_db
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovs_conf_db
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovs_sys_id_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovs_sys_id_conf
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovs_conf_db_lock
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovs_conf_db_lock
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovs_vswitchd_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovs_vswitchd_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_owner_ovsdb_server_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
  - name: file_groupowner_ovsdb_server_pid
    description: Ensure that the Container Network Interface file ownership is set
      to root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.10 - \[\] 1.1.10 Ensure that the Container Network Interface file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

### Rules:

  - file_owner_cni_conf
  - file_groupowner_cni_conf
  - file_owner_multus_conf
  - file_groupowner_multus_conf
  - file_owner_ip_allocations
  - file_groupowner_ip_allocations
  - file_owner_openshift_sdn_cniserver_config
  - file_groupowner_openshift_sdn_cniserver_config
  - file_owner_ovs_pid
  - file_groupowner_ovs_pid
  - file_owner_ovs_conf_db
  - file_groupowner_ovs_conf_db
  - file_owner_ovs_sys_id_conf
  - file_groupowner_ovs_sys_id_conf
  - file_owner_ovs_conf_db_lock
  - file_groupowner_ovs_conf_db_lock
  - file_owner_ovs_vswitchd_pid
  - file_groupowner_ovs_vswitchd_pid
  - file_owner_ovsdb_server_pid
  - file_groupowner_ovsdb_server_pid

### Implementation Status: planned

______________________________________________________________________
