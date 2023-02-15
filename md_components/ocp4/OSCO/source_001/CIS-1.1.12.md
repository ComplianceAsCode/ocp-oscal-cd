---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_owner_etcd_data_dir
      description: Ensure that the etcd data directory ownership is set to root:root
    - name: file_groupowner_etcd_data_dir
      description: Ensure that the etcd data directory ownership is set to root:root
    - name: file_owner_etcd_data_files
      description: Ensure that the etcd data directory ownership is set to root:root
    - name: file_groupowner_etcd_data_files
      description: Ensure that the etcd data directory ownership is set to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-1.1.12 - \[\] 1.1.12 Ensure that the etcd data directory ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.1.12 -->

### Rules:

  - file_owner_etcd_data_dir
  - file_groupowner_etcd_data_dir
  - file_owner_etcd_data_files
  - file_groupowner_etcd_data_files

### Implementation Status: planned

______________________________________________________________________
