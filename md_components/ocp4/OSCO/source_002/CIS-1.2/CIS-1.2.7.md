---
x-trestle-comp-def-rules:
  OSCO:
    - name: api_server_auth_mode_no_aa
      description: Ensure that the --authorization-mode argument is not set to AlwaysAllow
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.7 - \[API Server\] Ensure that the --authorization-mode argument is not set to AlwaysAllow

## Control Statement

Do not always authorize all requests.

## Control rationale_statement

The API Server, can be configured to allow all requests. This mode should not be used on any production cluster.

## Control impact_statement

Only authorized requests will be served.

## Control remediation_procedure

None. RBAC is always on and the OpenShift API server does not use the values assigned to the flag authorization-mode.

## Control audit_procedure

It is not possible to configure an OpenShift cluster to allow all requests. OpenShift is configured at bootstrap time to use RBAC to authorize requests. Role-based access control (RBAC) objects determine what actions a user is allowed to perform on what objects in an OpenShift cluster. Cluster administrators manage RBAC for the cluster. Project owners can manage RBAC for their individual OpenShift projects. The OpenShift API server configmap does not use the `authorization-mode` flag. 

To verify, run the following commands:

```
# To verify that the authorization-mode argument is not used 
oc get configmap config -n openshift-kube-apiserver -ojson | jq -r '.data["config.yaml"]' | jq '.apiServerArguments' 
oc get configmap config -n openshift-apiserver -ojson | jq -r '.data["config.yaml"]' | jq '.apiServerArguments' 

#Check that no overrides are configured
oc get kubeapiservers.operator.openshift.io cluster -o json | jq -r '.spec.unsupportedConfigOverrides'

# To verify RBAC is configured:
oc get clusterrolebinding
oc get clusterrole
oc get rolebinding
oc get role
```

## Control CIS_Controls

TITLE:Configure Data Access Control Lists CONTROL:v8 3.3 DESCRIPTION:Configure data access control lists based on a user’s need to know. Apply data access control lists, also known as access permissions, to local and remote file systems, databases, and applications.;TITLE:Ensure Only Approved Ports, Protocols and Services Are Running CONTROL:v7 9.2 DESCRIPTION:Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.7 -->

### Rules:

  - api_server_auth_mode_no_aa

### Implementation Status: planned

______________________________________________________________________
