---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_tls_cert
      description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
        are set as appropriate
    - name: api_server_tls_private_key
      description: Ensure that the --tls-cert-file and --tls-private-key-file arguments
        are set as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.30 - \[\] 1.2.30 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.30 -->

### Rules:

  - api_server_tls_cert
  - api_server_tls_private_key

### Implementation Status: planned

______________________________________________________________________
