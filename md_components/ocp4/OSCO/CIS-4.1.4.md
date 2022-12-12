---
x-trestle-comp-def-rules:
  - name: file_owner_proxy_kubeconfig
    description: If proxy kubeconfig file exists ensure ownership is set to root:root
      (Manual)
  - name: file_groupowner_proxy_kubeconfig
    description: If proxy kubeconfig file exists ensure ownership is set to root:root
      (Manual)
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-4.1.4 - \[\] 4.1.4 If proxy kubeconfig file exists ensure ownership is set to root:root (Manual)

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - file_owner_proxy_kubeconfig
  - file_groupowner_proxy_kubeconfig

### Implementation Status: planned

______________________________________________________________________
