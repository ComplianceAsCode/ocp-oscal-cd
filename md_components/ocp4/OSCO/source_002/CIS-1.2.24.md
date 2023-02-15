---
x-trestle-comp-def-rules:
  OSCO:
    - name: api_server_audit_log_maxbackup
      description: Ensure that the --audit-log-maxbackup argument is set to 10 or
        as appropriate
    - name: ocp_api_server_audit_log_maxbackup
      description: Ensure that the --audit-log-maxbackup argument is set to 10 or
        as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.24 - \[\] 1.2.24 Ensure that the --audit-log-maxbackup argument is set to 10 or as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.24 -->

### Rules:

  - api_server_audit_log_maxbackup
  - ocp_api_server_audit_log_maxbackup

### Implementation Status: planned

______________________________________________________________________
