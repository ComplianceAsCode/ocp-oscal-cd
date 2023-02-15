---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_permissions_openshift_pki_cert_files
      description: Ensure that the OpenShift PKI certificate file permissions are
        set to 644 or more restrictive
    - name: file_permissions_etcd_pki_cert_files
      description: Ensure that the OpenShift PKI certificate file permissions are
        set to 644 or more restrictive
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-1.1.20 - \[\] 1.1.20 Ensure that the OpenShift PKI certificate file permissions are set to 644 or more restrictive

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.1.20 -->

### Rules:

  - file_permissions_openshift_pki_cert_files
  - file_permissions_etcd_pki_cert_files

### Implementation Status: planned

______________________________________________________________________
