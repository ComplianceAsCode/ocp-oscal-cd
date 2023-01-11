---
x-trestle-comp-def-rules:
  - name: secrets_no_environment_variables
    description: Prefer using secrets as files over secrets as environment variables
      (info)
x-trestle-comp-def-rules-param-vals:
  kubelet_eviction_thresholds_set_soft_memory_available: 500Mi
  kubelet_eviction_thresholds_set_soft_nodefs_available: 10%
  kubelet_eviction_thresholds_set_soft_nodefs_inodesfree: 5%
  kubelet_eviction_thresholds_set_soft_imagefs_available: 15%
  kubelet_eviction_thresholds_set_soft_imagefs_inodesfree: 10%
  kubelet_eviction_thresholds_set_hard_memory_available: 200Mi
  kubelet_eviction_thresholds_set_hard_nodefs_available: 5%
  kubelet_eviction_thresholds_set_hard_nodefs_inodesfree: 4%
  kubelet_eviction_thresholds_set_hard_imagefs_available: 10%
  kubelet_eviction_thresholds_set_hard_imagefs_inodesfree: 5%
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-5.4.1 - \[\] 5.4.1 Prefer using secrets as files over secrets as environment variables (info)

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-5.4.1

### Rules:

  - secrets_no_environment_variables

### Implementation Status: planned

______________________________________________________________________
