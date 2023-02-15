---
x-trestle-comp-def-rules:
  OCP4:
    - name: kubelet_enable_streaming_connections
      description: Ensure that the --streaming-connection-idle-timeout argument is
        not set to 0
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-4.2.5 - \[\] 4.2.5 Ensure that the --streaming-connection-idle-timeout argument is not set to 0

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.2.5 -->

### Rules:

  - kubelet_enable_streaming_connections

### Implementation Status: planned

______________________________________________________________________
