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
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-4.2.10 - \[\] 4.2.10 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - kubelet_configure_tls_cert
  - kubelet_configure_tls_cert_pre_4_9
  - kubelet_configure_tls_key
  - kubelet_configure_tls_key_pre_4_9

### Implementation Status: planned

______________________________________________________________________
