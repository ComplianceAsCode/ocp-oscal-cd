---
x-trestle-comp-def-rules:
  OCP4:
    - name: api_server_etcd_ca
      description: Ensure that the --etcd-cafile argument is set as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.32 - \[API Server\] Ensure that the --etcd-cafile argument is set as appropriate

## Control Statement

`etcd` should be configured to make use of TLS encryption for client connections.

## Control rationale_statement

`etcd` is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be protected by client authentication. This requires the API server to identify itself to the `etcd` server using a SSL Certificate Authority file.

## Control impact_statement

TLS and client certificate authentication must be configured for `etcd`.

## Control remediation_procedure

None required. OpenShift generates the `etcd-cafile` and sets the arguments appropriately in the API server. Communication with `etcd` is secured by the `etcd` serving CA.

## Control audit_procedure

OpenShift uses X.509 certificates to provide secure communication to `etcd`. OpenShift does not use values assigned to the `etcd-cafile` argument. OpenShift generates the `etcd-cafile` and sets the arguments appropriately in the API server. OpenShift includes multiple certificate authorities (CAs) providing independent chains of trust, increasing the security posture of the cluster. The certificates generated by each CA are used to identify a particular OpenShift platform component to another OpenShift platform component. Communication with `etcd` is secured by the `etcd` serving CA.

Run the following command

```
# etcd CA File
oc get configmap config -n openshift-kube-apiserver -ojson | \
 jq -r '.data["config.yaml"]' | \
 jq -r .storageConfig.ca

# for ocp 4.6 replace jq -r .storageConfig.ca with
 jq -r '.apiServerArguments["etcd-cafile"]'
```

Verify that the following is returned

`/etc/kubernetes/static-pod-resources/configmaps/etcd-serving-ca/ca-bundle.crt`

## Control CIS_Controls

TITLE:Encrypt Sensitive Data in Transit CONTROL:v8 3.10 DESCRIPTION:Encrypt sensitive data in transit. Example implementations can include: Transport Layer Security (TLS) and Open Secure Shell (OpenSSH).;TITLE:Encrypt All Sensitive Information in Transit CONTROL:v7 14.4 DESCRIPTION:Encrypt all sensitive information in transit.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.32 -->

### Rules:

  - api_server_etcd_ca

### Implementation Status: planned

______________________________________________________________________
