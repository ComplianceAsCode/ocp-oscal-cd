---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_admission_control_plugin_ServiceAccount
      description: Ensure that the admission control plugin ServiceAccount is set
    - name: api_server_no_adm_ctrl_plugins_disabled
      description: Ensure that the admission control plugin ServiceAccount is set
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.14 - \[\] 1.2.14 Ensure that the admission control plugin ServiceAccount is set

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.14 -->

### Rules:

  - api_server_admission_control_plugin_ServiceAccount
  - api_server_no_adm_ctrl_plugins_disabled

### Implementation Status: planned

______________________________________________________________________
