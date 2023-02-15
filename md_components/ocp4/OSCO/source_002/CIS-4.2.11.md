---
x-trestle-comp-def-rules:
  OSCO:
    - name: kubelet_enable_client_cert_rotation
      description: Ensure that the --rotate-certificates argument is not set to false
    - name: kubelet_enable_cert_rotation
      description: Ensure that the --rotate-certificates argument is not set to false
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-4.2.11 - \[\] 4.2.11 Ensure that the --rotate-certificates argument is not set to false

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.2.11 -->

### Rules:

  - kubelet_enable_client_cert_rotation
  - kubelet_enable_cert_rotation

### Implementation Status: planned

______________________________________________________________________
