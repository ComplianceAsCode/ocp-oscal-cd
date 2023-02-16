---
x-trestle-comp-def-rules:
  OSCO:
    - name: controller_service_account_ca
      description: Ensure that the --root-ca-file argument is set as appropriate
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.3.5 - \[Controller Manager\] Ensure that the --root-ca-file argument is set as appropriate

## Control Statement

Allow pods to verify the API server's serving certificate before establishing connections.

## Control rationale_statement

Processes running within pods that need to contact the API server must verify the API server's serving certificate. Failing to do so could be a subject to man-in-the-middle attacks.

Providing the root certificate for the API server's serving certificate to the controller manager with the `--root-ca-file` argument allows the controller manager to inject the trusted bundle into pods so that they can verify TLS connections to the API server.

## Control impact_statement

OpenShift clusters manage and maintain certificate authorities and certificates for cluster components.

## Control remediation_procedure

None required. Certificates for OpenShift platform components are automatically created and rotated by the OpenShift Container Platform.

## Control audit_procedure

Certificates for OpenShift platform components are automatically created and rotated by the OpenShift Container Platform. 

Run the following command:

```
oc get configmaps config -n openshift-kube-controller-manager -ojson | \
 jq -r '.data["config.yaml"]' | \
 jq -r '.extendedArguments["root-ca-file"][]'
```

Verify that the `--root-ca-file` argument exists and is set to `/etc/kubernetes/static-pod-resources/configmaps/serviceaccount-ca/ca-bundle.crt`.

## Control CIS_Controls

TITLE:Perform Application Layer Filtering CONTROL:v8 13.10 DESCRIPTION:Perform application layer filtering. Example implementations include a filtering proxy, application layer firewall, or gateway.;TITLE:Use Unique Passwords CONTROL:v7 4.4 DESCRIPTION:Where multi-factor authentication is not supported (such as local administrator, root, or service accounts), accounts will use passwords that are unique to that system.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.3.5 -->

### Rules:

  - controller_service_account_ca

### Implementation Status: planned

______________________________________________________________________
