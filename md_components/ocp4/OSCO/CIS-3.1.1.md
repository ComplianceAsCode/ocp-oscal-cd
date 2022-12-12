---
x-trestle-comp-def-rules:
  - name: idp_is_configured
    description: Client certificate authentication should not be used for users
  - name: kubeadmin_removed
    description: Client certificate authentication should not be used for users
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-3.1.1 - \[\] 3.1.1 Client certificate authentication should not be used for users

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - idp_is_configured
  - kubeadmin_removed

### Implementation Status: planned

______________________________________________________________________
