---
x-trestle-comp-def-rules:
  - name: file_owner_kube_controller_manager
    description: Ensure that the controller manager pod specification file ownership
      is set to root:root
  - name: file_groupowner_kube_controller_manager
    description: Ensure that the controller manager pod specification file ownership
      is set to root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.4 - \[\] 1.1.4 Ensure that the controller manager pod specification file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - file_owner_kube_controller_manager
  - file_groupowner_kube_controller_manager

### Implementation Status: planned

______________________________________________________________________
