---
x-trestle-comp-def-rules:
  - name: kubelet_configure_tls_cert
    description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
      are set as appropriate
  - name: kubelet_configure_tls_cert_pre_4_9
    description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
      are set as appropriate
  - name: kubelet_configure_tls_key
    description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
      are set as appropriate
  - name: kubelet_configure_tls_key_pre_4_9
    description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
      are set as appropriate
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

# CIS-4.2.10 - \[\] 4.2.10 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

Add control implementation description here for control CIS-4.2.10

### Rules:

  - kubelet_configure_tls_cert
  - kubelet_configure_tls_cert_pre_4_9
  - kubelet_configure_tls_key
  - kubelet_configure_tls_key_pre_4_9

### Implementation Status: planned

______________________________________________________________________
