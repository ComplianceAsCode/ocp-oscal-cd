---
x-trestle-comp-def-rules:
  OSCO:
    - name: idp_is_configured
      description: Client certificate authentication should not be used for users
    - name: kubeadmin_removed
      description: Client certificate authentication should not be used for users
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-3.1.1 - \[\] 3.1.1 Client certificate authentication should not be used for users

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-3.1.1 -->

### Rules:

  - idp_is_configured
  - kubeadmin_removed

### Implementation Status: planned

______________________________________________________________________
