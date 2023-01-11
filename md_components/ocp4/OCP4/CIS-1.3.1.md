---
x-trestle-comp-def-rules:
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
x-trestle-rules-params:
  - name: kubelet_eviction_thresholds_set_soft_memory_available
    description: Memory Available for the EvictionSoft threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_soft_memory_available
    options: "{'default': '500Mi'}"
  - name: kubelet_eviction_thresholds_set_soft_nodefs_available
    description: Node FS Available for the EvictionSoft threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_soft_nodefs_available
    options: "{'default': '10%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_soft_nodefs_inodesfree
    description: Node FS inodes Free for the EvictionSoft threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_soft_nodefs_inodesfree
    options: "{'default': '5%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_soft_imagefs_available
    description: Image FS Available for the EvictionSoft threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_soft_imagefs_available
    options: "{'default': '15%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_soft_imagefs_inodesfree
    description: Image FS inodes Free for the EvictionSoft threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_soft_imagefs_inodesfree
    options: "{'default': '10%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_hard_memory_available
    description: Memory Available for the EvictonHard threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_hard_memory_available
    options: "{'default': '200Mi'}"
  - name: kubelet_eviction_thresholds_set_hard_nodefs_available
    description: Node FS Available for the EvictonHard threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_hard_nodefs_available
    options: "{'default': '5%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_hard_nodefs_inodesfree
    description: Node FS inodes Free for the EvictonHard threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_hard_nodefs_inodesfree
    options: "{'default': '4%', '4pc': '4%', '5pc': '5%', '10pc': '10%', '15pc': '15%',\
      \ '20pc': '20%'}"
  - name: kubelet_eviction_thresholds_set_hard_imagefs_available
    description: Image FS Available for the EvictonHard threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_hard_imagefs_available
    options: "{'default': '10%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
  - name: kubelet_eviction_thresholds_set_hard_imagefs_inodesfree
    description: Image FS inodes Free for the EvictonHard threshold to trigger.
    rule-id: kubelet_eviction_thresholds_set_hard_imagefs_inodesfree
    options: "{'default': '5%', '5pc': '5%', '10pc': '10%', '15pc': '15%', '20pc':\
      \ '20%'}"
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

# CIS-1.3.1 - \[\] 1.3.1 Ensure that garbage collection is configured as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.3.1

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
