---
x-trestle-comp-def-rules:
  - name: file_owner_etcd_member
    description: Ensure that the etcd pod specification file ownership is set to root:root
      (Automated)
  - name: file_groupowner_etcd_member
    description: Ensure that the etcd pod specification file ownership is set to root:root
      (Automated)
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.8 - \[\] 1.1.8 Ensure that the etcd pod specification file ownership is set to root:root (Automated)

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.1.8

### Rules:

  - file_owner_etcd_member
  - file_groupowner_etcd_member

### Implementation Status: planned

______________________________________________________________________
