---
x-trestle-comp-def-rules:
  OSCO:
    - name: api_server_admission_control_plugin_NamespaceLifecycle
      description: Ensure that the admission control plugin NamespaceLifecycle is
        set
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-1.2.15 - \[API Server\] Ensure that the admission control plugin NamespaceLifecycle is set

## Control Statement

Reject creating objects in a namespace that is undergoing termination.

## Control rationale_statement

Setting admission control policy to `NamespaceLifecycle` ensures that objects cannot be created in non-existent namespaces, and that namespaces undergoing termination are not used for creating the new objects. This is recommended to enforce the integrity of the namespace termination process and also for the availability of the newer objects.

## Control impact_statement

None

## Control remediation_procedure

Ensure that the `--disable-admission-plugins` parameter does not include `NamespaceLifecycle`.

## Control audit_procedure

OpenShift enables the `NamespaceLifecycle` plugin by default.

Run the following command:

```
#Verify the list of admission controllers for 4.6 and higher
oc -n openshift-kube-apiserver get configmap config -o json | jq -r '.data."config.yaml"' | jq '.apiServerArguments."enable-admission-plugins"'

#Check that no overrides are configured
oc get kubeapiservers.operator.openshift.io cluster -o json | jq -r '.spec.unsupportedConfigOverrides'
```

In OCP 4.5 and earlier, the default set of admission plugins are compiled into the `apiserver` and are not visible in the configuration yaml. 

For 4.6 and above, verify that the set of admission plugins includes `NamespaceLifecycle` and that the `--disable-admission-plugins` argument is set to a value that does not include `NamespaceLifecycle`. 

Verify that no unsupported Overrides are configured.

## Control CIS_Controls

TITLE:Establish and Maintain a Secure Configuration Process CONTROL:v8 4.1 DESCRIPTION:Establish and maintain a secure configuration process for enterprise assets (end-user devices, including portable and mobile, non-computing/IoT devices, and servers) and software (operating systems and applications). Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.;TITLE:Protect Information through Access Control Lists CONTROL:v7 14.6 DESCRIPTION:Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.2.15 -->

### Rules:

  - api_server_admission_control_plugin_NamespaceLifecycle

### Implementation Status: planned

______________________________________________________________________
