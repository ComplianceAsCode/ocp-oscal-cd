---
x-trestle-comp-def-rules:
  - name: file_groupowner_kubelet_conf
    description: Ensure that the --kubeconfig kubelet.conf file ownership is set to
      root:root
  - name: file_groupowner_kubelet
    description: Ensure that the --kubeconfig kubelet.conf file ownership is set to
      root:root
  - name: file_owner_kubelet_conf
    description: Ensure that the --kubeconfig kubelet.conf file ownership is set to
      root:root
  - name: file_owner_kubelet
    description: Ensure that the --kubeconfig kubelet.conf file ownership is set to
      root:root
x-trestle-global:
  profile-title: OCP4 CIS Node Profile
---

# CIS-4.1.6 - \[\] 4.1.6 Ensure that the --kubeconfig kubelet.conf file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

### Rules:

  - file_groupowner_kubelet_conf
  - file_groupowner_kubelet
  - file_owner_kubelet_conf
  - file_owner_kubelet

### Implementation Status: planned

______________________________________________________________________
