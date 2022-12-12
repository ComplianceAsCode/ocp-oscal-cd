---
x-trestle-comp-def-rules:
  - name: file_owner_worker_service
    description: Ensure that the kubelet service file ownership is set to root:root
  - name: file_groupowner_worker_service
    description: Ensure that the kubelet service file ownership is set to root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-4.1.2 - \[\] 4.1.2 Ensure that the kubelet service file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - file_owner_worker_service
  - file_groupowner_worker_service

### Implementation Status: planned

______________________________________________________________________
