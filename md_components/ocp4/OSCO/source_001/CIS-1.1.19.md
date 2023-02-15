---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_owner_openshift_pki_key_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
    - name: file_groupowner_openshift_pki_key_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
    - name: file_owner_openshift_pki_cert_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
    - name: file_groupowner_openshift_pki_cert_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
    - name: file_owner_etcd_pki_cert_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
    - name: file_groupowner_etcd_pki_cert_files
      description: Ensure that the OpenShift PKI directory and file ownership is set
        to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-1.1.19 - \[\] 1.1.19 Ensure that the OpenShift PKI directory and file ownership is set to root:root

## Control Statement

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.1.19 -->

### Rules:

  - file_owner_openshift_pki_key_files
  - file_groupowner_openshift_pki_key_files
  - file_owner_openshift_pki_cert_files
  - file_groupowner_openshift_pki_cert_files
  - file_owner_etcd_pki_cert_files
  - file_groupowner_etcd_pki_cert_files

### Implementation Status: planned

______________________________________________________________________
