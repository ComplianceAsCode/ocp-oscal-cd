---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_api_priority_gate_enabled
      description: Ensure that the admission control plugin EventRateLimit is set
    - name: api_server_api_priority_flowschema_catch_all
      description: Ensure that the admission control plugin EventRateLimit is set
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.10 - \[\] 1.2.10 Ensure that the admission control plugin EventRateLimit is set

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.10 -->

### Rules:

  - api_server_api_priority_gate_enabled
  - api_server_api_priority_flowschema_catch_all

### Implementation Status: planned

______________________________________________________________________
