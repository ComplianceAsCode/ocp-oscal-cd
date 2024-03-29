---
x-trestle-comp-def-rules:
  OCP4:
    - name: kubelet_enable_protect_kernel_sysctl
      description: Ensure that the --protect-kernel-defaults argument is set to true
    - name: kubelet_enable_protect_kernel_defaults
      description: Ensure that the --protect-kernel-defaults argument is set to true
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-4.2.6 - \[Kubelet\] Ensure that the --protect-kernel-defaults argument is not set

## Control Statement

Protect tuned kernel parameters from overriding kubelet default kernel parameter values.

## Control rationale_statement

Kernel parameters are usually tuned and hardened by the system administrators before putting the systems into production. These parameters protect the kernel and the system. Your kubelet kernel defaults that rely on such parameters should be appropriately set to match the desired secured system state. Ignoring this could potentially lead to running pods with undesired kernel behavior.

## Control impact_statement

You would have to re-tune kernel parameters to match kubelet parameters.

## Control remediation_procedure

None required. The OpenShift 4 kubelet modifies the system tunable; using the `protect-kernel-defaults` flag will cause the kubelet to fail on start if the tunables don't match the kubelet configuration and the OpenShift node will fail to start.

## Control audit_procedure

The OpenShift 4 kubelet modifies the system tunable; using the `protect-kernel-defaults` flag will cause the kubelet to fail on start if the tunables don't match the kubelet configuration and the OpenShift node will fail to start.

Run the following command:

```
for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}'); do oc debug node/${node} -- chroot /host more /etc/kubernetes/kubelet.conf; done
```

Verify that protectKernelDefaults is not present.

## Control CIS_Controls

TITLE:Perform Automated Operating System Patch Management CONTROL:v8 7.3 DESCRIPTION:Perform operating system updates on enterprise assets through automated patch management on a monthly, or more frequent, basis.;TITLE:Deploy Automated Operating System Patch Management Tools CONTROL:v7 3.4 DESCRIPTION:Deploy automated software update tools in order to ensure that the operating systems are running the most recent security updates provided by the software vendor.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.2.6 -->

### Rules:

  - kubelet_enable_protect_kernel_sysctl
  - kubelet_enable_protect_kernel_defaults

### Implementation Status: planned

______________________________________________________________________
