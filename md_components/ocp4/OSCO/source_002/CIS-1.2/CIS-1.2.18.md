---
x-trestle-comp-def-rules:
  OSCO:
    - name: api_server_insecure_bind_address
      description: Ensure that the --insecure-bind-address argument is not set
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.18 - \[API Server\] Ensure that the --insecure-bind-address argument is not set

## Control Statement

Do not bind the insecure API service.

## Control rationale_statement

If you bind the `apiserver` to an insecure address, basically anyone who could connect to it over the insecure port, would have unauthenticated and unencrypted access to your master node. The `apiserver` doesn't do any authentication checking for insecure binds and traffic to the Insecure API port is not encrypted, allowing attackers to potentially read sensitive data in transit.

## Control impact_statement

Connections to the API server will require valid authentication credentials.

## Control remediation_procedure

None required.

## Control audit_procedure

The `openshift-kube-apiserver` is served over HTTPS with authentication and authorization; the secure API endpoint for the `penshift-kube-apiserver` is bound to `0.0.0.0:6443` by `default`. Note that the `openshift-apiserver` is not running in the host network namespace. The port is not exposed on the node, but only through the pod network.

Run the following command:

```
# InsecureBindAddress=true should not be in the results
oc get kubeapiservers.operator.openshift.io cluster -o jsonpath='{range .spec.observedConfig.apiServerArguments.feature-gates[*]}{@}{"\n"}{end}'

# Result should be only 6443
oc -n openshift-kube-apiserver get endpoints -o jsonpath='{.items[*].subsets[*].ports[*].port}'

# Result should be only 8443
oc -n openshift-apiserver get endpoints -o jsonpath='{.items[*].subsets[*].ports[*].port}'
```

Verify that the `--insecure-bind-address` argument does not exist.

Verify that the `bindAddress` is set to `6443` for the `openshift-kube-apiserver` and `8443` for the `openshift-apiserver`.

Note that the `openshift-apiserver` is not running in the host network namespace. The port is not exposed on the node, but only through the pod network.

## Control CIS_Controls

TITLE:Leverage Vetted Modules or Services for Application Security Components CONTROL:v8 16.11 DESCRIPTION:Leverage vetted modules or services for application security components, such as identity management, encryption, and auditing and logging. Using platform features in critical security functions will reduce developers’ workload and minimize the likelihood of design or implementation errors. Modern operating systems provide effective mechanisms for identification, authentication, and authorization and make those mechanisms available to applications. Use only standardized, currently accepted, and extensively reviewed encryption algorithms. Operating systems also provide mechanisms to create and maintain secure audit logs.;TITLE:Ensure Only Approved Ports, Protocols and Services Are Running CONTROL:v7 9.2 DESCRIPTION:Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.18 -->

### Rules:

  - api_server_insecure_bind_address

### Implementation Status: planned

______________________________________________________________________
