---
x-trestle-comp-def-rules:
  - name: api_server_https_for_kubelet_conn
    description: Ensure that the --kubelet-https argument is set to true
  - name: api_server_openshift_https_serving_cert
    description: Ensure that the --kubelet-https argument is set to true
  - name: api_server_oauth_https_serving_cert
    description: Ensure that the --kubelet-https argument is set to true
x-trestle-global:
  profile-title: OCP4 CIS Profile
---

# CIS-1.2.4 - \[\] 1.2.4 Ensure that the --kubelet-https argument is set to true

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Enter possible prose for implementation response at the control level here, after this comment -->

### Rules:

  - api_server_https_for_kubelet_conn
  - api_server_openshift_https_serving_cert
  - api_server_oauth_https_serving_cert

### Implementation Status: planned

______________________________________________________________________
