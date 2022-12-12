---
x-trestle-comp-def-rules:
  - name: kubelet_enable_protect_kernel_sysctl
    description: Ensure that the --protect-kernel-defaults argument is set to true
  - name: kubelet_enable_protect_kernel_defaults
    description: Ensure that the --protect-kernel-defaults argument is set to true
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-4.2.6 - \[\] 4.2.6 Ensure that the --protect-kernel-defaults argument is set to true

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - kubelet_enable_protect_kernel_sysctl
  - kubelet_enable_protect_kernel_defaults

### Implementation Status: planned

______________________________________________________________________
