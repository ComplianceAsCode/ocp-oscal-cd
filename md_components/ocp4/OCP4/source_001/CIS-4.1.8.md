---
x-trestle-comp-def-rules:
  OCP4:
    - name: file_owner_worker_ca
      description: Ensure that the client certificate authorities file ownership is
        set to root:root
    - name: file_groupowner_worker_ca
      description: Ensure that the client certificate authorities file ownership is
        set to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.1.8 - \[\] 4.1.8 Ensure that the client certificate authorities file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.1.8 -->

### Rules:

  - file_owner_worker_ca
  - file_groupowner_worker_ca

### Implementation Status: planned

______________________________________________________________________
