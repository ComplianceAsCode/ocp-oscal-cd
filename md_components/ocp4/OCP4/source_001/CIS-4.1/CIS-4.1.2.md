---
x-trestle-comp-def-rules:
  OCP4:
    - name: file_owner_worker_service
      description: Ensure that the kubelet service file ownership is set to root:root
    - name: file_groupowner_worker_service
      description: Ensure that the kubelet service file ownership is set to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.1.2 - \[Worker Node Configuration Files\] Ensure that the kubelet service file ownership is set to root:root

## Control Statement

Ensure that the kubelet service file ownership is set to `root:root`.

## Control rationale_statement

The kubelet service file controls various parameters that set the behavior of the kubelet service in the worker node. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Control impact_statement

None

## Control remediation_procedure

By default, the kubelet service file has ownership of `root:root`.

## Control audit_procedure

Run the following command:

```

# Should return root:root for each node
for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot /host stat -c %U:%G /etc/systemd/system/kubelet.service
done
```

Verify that the ownership is set to `root:root`.

## Control CIS_Controls

TITLE:Restrict Administrator Privileges to Dedicated Administrator Accounts CONTROL:v8 5.4 DESCRIPTION:Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.1.2 -->

### Rules:

  - file_owner_worker_service
  - file_groupowner_worker_service

### Implementation Status: planned

______________________________________________________________________
