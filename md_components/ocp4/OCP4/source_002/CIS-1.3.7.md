---
x-trestle-comp-def-rules:
  OCP4:
    - name: controller_secure_port
      description: Ensure that the --bind-address argument is set to 127.0.0.1
    - name: controller_insecure_port_disabled
      description: Ensure that the --bind-address argument is set to 127.0.0.1
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.3.7 - \[\] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.3.7 -->

### Rules:

  - controller_secure_port
  - controller_insecure_port_disabled

### Implementation Status: planned

______________________________________________________________________
