---
x-trestle-comp-def-rules:
  OSCO:
    - name: file_permissions_kubelet_conf
      description: Ensure that the --kubeconfig kubelet.conf file permissions are
        set to 644 or more restrictive
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.1.5 - \[Worker Node Configuration Files\] Ensure that the --kubeconfig kubelet.conf file permissions are set to 600 or more restrictive

## Control Statement

Ensure that the `kubelet.conf` file has permissions of `600` or more restrictive.

## Control rationale_statement

The `kubelet.conf` file is the kubeconfig file for the node, and controls various parameters that set the behavior and identity of the worker node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Control impact_statement

None

## Control remediation_procedure

run command:

```
chmod 600 /etc/kubernetes/kubelet.conf
```

## Control audit_procedure

The node's `kubeconfig` is created with `644` permissions. 

Run the following command:

```
# Check permissions
for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot /host stat -c %a /etc/kubernetes/kubelet.conf
done
```

Verify that the permissions are `600`.

## Control CIS_Controls

TITLE:Configure Data Access Control Lists CONTROL:v8 3.3 DESCRIPTION:Configure data access control lists based on a user’s need to know. Apply data access control lists, also known as access permissions, to local and remote file systems, databases, and applications.;TITLE:Protect Information through Access Control Lists CONTROL:v7 14.6 DESCRIPTION:Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.1.5 -->

### Rules:

  - file_permissions_kubelet_conf

### Implementation Status: planned

______________________________________________________________________
