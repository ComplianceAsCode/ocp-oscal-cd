---
x-trestle-comp-def-rules:
  OCP4:
    - name: kubelet_eviction_thresholds_set_soft_memory_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_soft_nodefs_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_soft_nodefs_inodesfree
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_soft_imagefs_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_soft_imagefs_inodesfree
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_hard_memory_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_hard_nodefs_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_hard_nodefs_inodesfree
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_hard_imagefs_available
      description: Ensure that garbage collection is configured as appropriate
    - name: kubelet_eviction_thresholds_set_hard_imagefs_inodesfree
      description: Ensure that garbage collection is configured as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.3.1 - \[\] 1.3.1 Ensure that garbage collection is configured as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.3.1 -->

### Rules:

  - kubelet_eviction_thresholds_set_soft_memory_available
  - kubelet_eviction_thresholds_set_soft_nodefs_available
  - kubelet_eviction_thresholds_set_soft_nodefs_inodesfree
  - kubelet_eviction_thresholds_set_soft_imagefs_available
  - kubelet_eviction_thresholds_set_soft_imagefs_inodesfree
  - kubelet_eviction_thresholds_set_hard_memory_available
  - kubelet_eviction_thresholds_set_hard_nodefs_available
  - kubelet_eviction_thresholds_set_hard_nodefs_inodesfree
  - kubelet_eviction_thresholds_set_hard_imagefs_available
  - kubelet_eviction_thresholds_set_hard_imagefs_inodesfree

### Implementation Status: planned

______________________________________________________________________
