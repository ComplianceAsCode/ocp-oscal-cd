---
x-trestle-comp-def-rules:
  OCP4:
    - name: file_owner_worker_kubeconfig
      description: Ensure that the kubelet configuration file ownership is set to
        root:root
    - name: file_groupowner_worker_kubeconfig
      description: Ensure that the kubelet configuration file ownership is set to
        root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.1.10 - \[Worker Node Configuration Files\] Ensure that the kubelet configuration file ownership is set to root:root

## Control Statement

Ensure that if the kubelet refers to a configuration file with the `--config` argument, that file is owned by `root:root`.

## Control rationale_statement

The kubelet reads various parameters, including security settings, from a config file specified by the `--config` argument. If this file is specified you should restrict its file permissions to maintain the integrity of the file. The file should be owned by `root:root`.

## Control impact_statement

None

## Control remediation_procedure

None required.

## Control audit_procedure

In OpenShift 4, the kublet config file is managed by the Machine Config Operator. The kubelet config file is found at `/var/lib/kubelet/kubeconfig` with ownership set to `root:root`.

Run the command:

```

for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot /host stat -c %U:%G /var/lib/kubelet/config.json
done
```

Verify that the ownership is set to `root:root`.

## Control CIS_Controls

TITLE:Restrict Administrator Privileges to Dedicated Administrator Accounts CONTROL:v8 5.4 DESCRIPTION:Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.1.10 -->

### Rules:

  - file_owner_worker_kubeconfig
  - file_groupowner_worker_kubeconfig

### Implementation Status: planned

______________________________________________________________________
