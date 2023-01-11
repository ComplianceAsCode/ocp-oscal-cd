---
x-trestle-comp-def-rules:
  - name: file_owner_scheduler_kubeconfig
    description: Ensure that the scheduler.conf file ownership is set to root:root
  - name: file_groupowner_scheduler_kubeconfig
    description: Ensure that the scheduler.conf file ownership is set to root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.16 - \[\] 1.1.16 Ensure that the scheduler.conf file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.1.16

### Rules:

  - file_owner_scheduler_kubeconfig
  - file_groupowner_scheduler_kubeconfig

### Implementation Status: planned

______________________________________________________________________
