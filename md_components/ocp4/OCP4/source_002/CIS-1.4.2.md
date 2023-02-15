---
x-trestle-comp-def-rules:
  OCP4:
    - name: scheduler_no_bind_address
      description: Ensure that the --bind-address argument is set to 127.0.0.1
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.4.2 - \[\] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.4.2 -->

### Rules:

  - scheduler_no_bind_address

### Implementation Status: planned

______________________________________________________________________