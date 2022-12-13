---
x-trestle-comp-def-rules:
  - name: file_owner_controller_manager_kubeconfig
    description: Ensure that the controller-manager.conf file ownership is set to
      root:root
  - name: file_groupowner_controller_manager_kubeconfig
    description: Ensure that the controller-manager.conf file ownership is set to
      root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-1.1.18 - \[\] 1.1.18 Ensure that the controller-manager.conf file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

### Rules:

  - file_owner_controller_manager_kubeconfig
  - file_groupowner_controller_manager_kubeconfig

### Implementation Status: planned

______________________________________________________________________
