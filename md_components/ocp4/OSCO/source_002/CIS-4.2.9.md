---
x-trestle-comp-def-rules:
  OSCO:
    - name: kubelet_configure_event_creation
      description: Ensure that the --event-qps argument is set to 0 or a level which
        ensures appropriate event capture
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-4.2.9 - \[\] 4.2.9 Ensure that the --event-qps argument is set to 0 or a level which ensures appropriate event capture

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.2.9 -->

### Rules:

  - kubelet_configure_event_creation

### Implementation Status: planned

______________________________________________________________________
