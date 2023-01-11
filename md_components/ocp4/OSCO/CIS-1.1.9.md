---
x-trestle-comp-def-rules:
  - name: file_permissions_cni_conf
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_multus_conf
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ip_allocations
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_perms_openshift_sdn_cniserver_config
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovs_pid
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovs_conf_db
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovs_sys_id_conf
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovs_conf_db_lock
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovs_vswitchd_pid
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
  - name: file_permissions_ovsdb_server_pid
    description: Ensure that the Container Network Interface file permissions are
      set to 644 or more restrictive
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.9 - \[\] 1.1.9 Ensure that the Container Network Interface file permissions are set to 644 or more restrictive

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.1.9

### Rules:

  - file_permissions_cni_conf
  - file_permissions_multus_conf
  - file_permissions_ip_allocations
  - file_perms_openshift_sdn_cniserver_config
  - file_permissions_ovs_pid
  - file_permissions_ovs_conf_db
  - file_permissions_ovs_sys_id_conf
  - file_permissions_ovs_conf_db_lock
  - file_permissions_ovs_vswitchd_pid
  - file_permissions_ovsdb_server_pid

### Implementation Status: planned

______________________________________________________________________
