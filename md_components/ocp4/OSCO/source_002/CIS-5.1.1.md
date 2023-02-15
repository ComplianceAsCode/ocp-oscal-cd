---
x-trestle-comp-def-rules:
  OSCO:
    - name: rbac_limit_cluster_admin
      description: Ensure that the cluster-admin role is only used where required
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-5.1.1 - \[\] 5.1.1 Ensure that the cluster-admin role is only used where required

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-5.1.1 -->

### Rules:

  - rbac_limit_cluster_admin

### Implementation Status: planned

______________________________________________________________________