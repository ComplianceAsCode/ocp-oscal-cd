---
x-trestle-comp-def-rules:
  - name: audit_log_forwarding_enabled
    description: Ensure that the audit logs are forwarded off the cluster for retention
x-trestle-comp-def-rules-param-vals:
  var_kubelet_eviction_thresholds_set_soft_memory_available: 500Mi
  var_kubelet_eviction_thresholds_set_soft_nodefs_available: 10%
  var_kubelet_eviction_thresholds_set_soft_nodefs_inodesfree: 5%
  var_kubelet_eviction_thresholds_set_soft_imagefs_available: 15%
  var_kubelet_eviction_thresholds_set_soft_imagefs_inodesfree: 10%
  var_kubelet_eviction_thresholds_set_hard_memory_available: 200Mi
  var_kubelet_eviction_thresholds_set_hard_nodefs_available: 5%
  var_kubelet_eviction_thresholds_set_hard_nodefs_inodesfree: 4%
  var_kubelet_eviction_thresholds_set_hard_imagefs_available: 10%
  var_kubelet_eviction_thresholds_set_hard_imagefs_inodesfree: 5%
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-1.2.23 - \[\] 1.2.23 Ensure that the audit logs are forwarded off the cluster for retention

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-1.2.23

### Rules:

  - audit_log_forwarding_enabled

### Implementation Status: planned

______________________________________________________________________
