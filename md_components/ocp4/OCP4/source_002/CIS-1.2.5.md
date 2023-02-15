---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_kubelet_client_cert
      description: Ensure that the --kubelet-client-certificate and --kubelet-client-key
        arguments are set as appropriate
    - name: api_server_kubelet_client_cert_pre_4_9
      description: Ensure that the --kubelet-client-certificate and --kubelet-client-key
        arguments are set as appropriate
    - name: api_server_kubelet_client_key
      description: Ensure that the --kubelet-client-certificate and --kubelet-client-key
        arguments are set as appropriate
    - name: api_server_kubelet_client_key_pre_4_9
      description: Ensure that the --kubelet-client-certificate and --kubelet-client-key
        arguments are set as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.5 - \[\] 1.2.5 Ensure that the --kubelet-client-certificate and --kubelet-client-key arguments are set as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.5 -->

### Rules:

  - api_server_kubelet_client_cert
  - api_server_kubelet_client_cert_pre_4_9
  - api_server_kubelet_client_key
  - api_server_kubelet_client_key_pre_4_9

### Implementation Status: planned

______________________________________________________________________
