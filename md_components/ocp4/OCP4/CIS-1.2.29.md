---
x-trestle-comp-def-rules:
  - name: api_server_etcd_cert
    description: Ensure that the --etcd-certfile and --etcd-keyfile arguments are
      set as appropriate
  - name: api_server_etcd_key
    description: Ensure that the --etcd-certfile and --etcd-keyfile arguments are
      set as appropriate
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

# CIS-1.2.29 - \[\] 1.2.29 Ensure that the --etcd-certfile and --etcd-keyfile arguments are set as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.2.29

### Rules:

  - api_server_etcd_cert
  - api_server_etcd_key

### Implementation Status: planned

______________________________________________________________________
