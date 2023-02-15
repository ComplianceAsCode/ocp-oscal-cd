---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_audit_log_maxsize
      description: Ensure that the --audit-log-maxsize argument is set to 100 or as
        appropriate
    - name: ocp_api_server_audit_log_maxsize
      description: Ensure that the --audit-log-maxsize argument is set to 100 or as
        appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.25 - \[\] 1.2.25 Ensure that the --audit-log-maxsize argument is set to 100 or as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.25 -->

### Rules:

  - api_server_audit_log_maxsize
  - ocp_api_server_audit_log_maxsize

### Implementation Status: planned

______________________________________________________________________
