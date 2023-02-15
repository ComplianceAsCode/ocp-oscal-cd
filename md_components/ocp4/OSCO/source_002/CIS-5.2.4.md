---
x-trestle-comp-def-rules:
  OSCO:
    - name: scc_limit_network_namespace
      description: Minimize the admission of containers wishing to share the host
        network namespace (info)
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-5.2.4 - \[\] 5.2.4 Minimize the admission of containers wishing to share the host network namespace (info)

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-5.2.4 -->

### Rules:

  - scc_limit_network_namespace

### Implementation Status: planned

______________________________________________________________________
