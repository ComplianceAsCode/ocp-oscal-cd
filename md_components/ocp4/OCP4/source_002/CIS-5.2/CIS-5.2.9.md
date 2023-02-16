---
x-trestle-comp-def-rules:
  OCP4:
    - name: scc_drop_container_capabilities
      description: Minimize the admission of containers with capabilities assigned
        (info)
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-5.2.9 - \[Pod Security Policies\] Minimize the admission of containers with capabilities assigned

## Control Statement

Do not generally permit containers with capabilities

## Control rationale_statement

Containers run with a default set of capabilities as assigned by the Container Runtime. Capabilities are parts of the rights generally granted on a Linux system to the root user.

In many cases applications running in containers do not require any capabilities to operate, so from the perspective of the principal of least privilege use of capabilities should be minimized.

## Control impact_statement

Pods with containers which require capabilities to operate will not be permitted.

## Control remediation_procedure

Review the use of capabilities in applications running on your cluster. Where a namespace contains applications which do not require any Linux capabilities to operate consider adding a SCC which forbids the admission of containers which do not drop all capabilities.

## Control audit_procedure

Get the set of SCCs with the following command:

```
oc get scc
```

For each SCC, check whether capabilities have been forbidden:

```
oc describe scc <name> | grep “Required Drop Capabilities”

for i in `oc get scc --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'`; do echo "$i"; oc describe scc $i | grep "Required Drop Capabilities"; done
```

## Control CIS_Controls

TITLE:Uninstall or Disable Unnecessary Services on Enterprise Assets and Software CONTROL:v8 4.8 DESCRIPTION:Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function.;TITLE:Maintain Secure Images CONTROL:v7 5.2 DESCRIPTION:Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-5.2.9 -->

### Rules:

  - scc_drop_container_capabilities

### Implementation Status: planned

______________________________________________________________________
