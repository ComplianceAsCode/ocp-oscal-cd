---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_owner_worker_ca
      description: Ensure that the client certificate authorities file ownership is
        set to root:root
    - name: file_groupowner_worker_ca
      description: Ensure that the client certificate authorities file ownership is
        set to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.1.8 - \[Worker Node Configuration Files\] Ensure that the client certificate authorities file ownership is set to root:root

## Control Statement

Ensure that the certificate authorities file ownership is set to `root:root`.

## Control rationale_statement

The certificate authorities file controls the authorities used to validate API requests. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Control impact_statement

None

## Control remediation_procedure

None required.

## Control audit_procedure

The Client CA location for the `kubelet` is defined in `/etc/kubernetes/kubelet.conf`. The 
`/etc/kubernetes/kubelet-ca.crt` file has ownership `root:root`.

Run the following command:

```

for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot /host stat -c %U:%G /etc/kubernetes/ca.pem
done
```

Verify that the ownership is set to `root:root`.

## Control CIS_Controls

TITLE:Restrict Administrator Privileges to Dedicated Administrator Accounts CONTROL:v8 5.4 DESCRIPTION:Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.1.8 -->

### Rules:

  - file_owner_worker_ca
  - file_groupowner_worker_ca

### Implementation Status: planned

______________________________________________________________________
