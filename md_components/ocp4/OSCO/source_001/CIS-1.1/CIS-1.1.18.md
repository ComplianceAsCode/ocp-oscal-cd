---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_owner_controller_manager_kubeconfig
      description: Ensure that the controller-manager.conf file ownership is set to
        root:root
    - name: file_groupowner_controller_manager_kubeconfig
      description: Ensure that the controller-manager.conf file ownership is set to
        root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-1.1.18 - \[Master Node Configuration Files\] Ensure that the controller-manager.conf file ownership is set to root:root

## Control Statement

Ensure that the `controller-manager.conf` file ownership is set to `root:root`.

## Control rationale_statement

The `controller-manager.conf` file is the `kubeconfig` file for the Controller Manager. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Control impact_statement

None

## Control remediation_procedure

No remediation required; file permissions are managed by the operator.

## Control audit_procedure

Run the following command:

```
for i in $(oc get pods -n openshift-kube-controller-manager -l app=kube-controller-manager -oname)
 do
 oc exec -n openshift-kube-controller-manager $i -- \
 stat -c %U:%G /etc/kubernetes/static-pod-resources/configmaps/controller-manager-kubeconfig/kubeconfig
 done
```

Verify that the ownership is set to `root:root`.

## Control CIS_Controls

TITLE:Restrict Administrator Privileges to Dedicated Administrator Accounts CONTROL:v8 5.4 DESCRIPTION:Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.;TITLE:Ensure the Use of Dedicated Administrative Accounts CONTROL:v7 4.3 DESCRIPTION:Ensure that all users with administrative account access use a dedicated or secondary account for elevated activities. This account should only be used for administrative activities and not internet browsing, email, or similar activities.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.1.18 -->

### Rules:

  - file_owner_controller_manager_kubeconfig
  - file_groupowner_controller_manager_kubeconfig

### Implementation Status: planned

______________________________________________________________________
