---
x-trestle-comp-def-rules:
  OSCO:
    - name: kubelet_enable_client_cert_rotation
      description: Ensure that the --rotate-certificates argument is not set to false
    - name: kubelet_enable_cert_rotation
      description: Ensure that the --rotate-certificates argument is not set to false
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-4.2.11 - \[Kubelet\] Ensure that the --rotate-certificates argument is not set to false

## Control Statement

Enable kubelet client certificate rotation.

## Control rationale_statement

The `--rotate-certificates` setting causes the kubelet to rotate its client certificates by creating new CSRs as its existing credentials expire. This automated periodic rotation ensures that the there is no downtime due to expired certificates and thus addressing availability in the CIA security triad.

Note: This recommendation only applies if you let kubelets get their certificates from the API server. In case your kubelet certificates come from an outside authority/tool (e.g. Vault) then you need to take care of rotation yourself.

## Control impact_statement

None

## Control remediation_procedure

None required.

## Control audit_procedure

This feature also requires the `RotateKubeletClientCertificate` feature gate to be enabled. The feature gate is enabled by default.

Run the following commands:

```

#Verify the rotateKubeletClientCertificate feature gate is not set to false
for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot /host cat /etc/kubernetes/kubelet.conf | grep RotateKubeletClientCertificate
done

# Verify the rotateCertificates argument is set to true
for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}')
do
 oc debug node/${node} -- chroot host grep rotate /etc/kubernetes/kubelet.conf;
done
```

Verify that the `rotateKubeletClientCertificates` feature gate argument is not set to `false`.

Verify that the `rotateCertificates` argument is set to `true`.

## Control CIS_Controls

TITLE:Encrypt Sensitive Data in Transit CONTROL:v8 3.10 DESCRIPTION:Encrypt sensitive data in transit. Example implementations can include: Transport Layer Security (TLS) and Open Secure Shell (OpenSSH).;TITLE:Encrypt All Sensitive Information in Transit CONTROL:v7 14.4 DESCRIPTION:Encrypt all sensitive information in transit.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-4.2.11 -->

### Rules:

  - kubelet_enable_client_cert_rotation
  - kubelet_enable_cert_rotation

### Implementation Status: planned

______________________________________________________________________
