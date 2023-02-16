---
x-trestle-comp-def-rules:
  OSCO:
    - name: secrets_no_environment_variables
      description: Prefer using secrets as files over secrets as environment variables
        (info)
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-5.4.1 - \[Secrets Management\] Prefer using secrets as files over secrets as environment variables

## Control Statement

Kubernetes supports mounting secrets as data volumes or as environment variables. Minimize the use of environment variable secrets.

## Control rationale_statement

It is reasonably common for application code to log out its environment (particularly in the event of an error). This will include any secret values passed in as environment variables, so secrets can easily be exposed to any user or entity who has access to the logs.

## Control impact_statement

Application code which expects to read secrets in the form of environment variables would need modification

## Control remediation_procedure

If possible, rewrite application code to read secrets from mounted secret files, rather than from environment variables.

## Control audit_procedure

Information about ways to provide sensitive data to pods is included in the documentation. 
[Providing sensitive data to pods](https://docs.openshift.com/container-platform/4.5/nodes/pods/nodes-pods-secrets.html)
Run the following command to find references to objects which use environment variables defined from secrets.

```
oc get all -o jsonpath='{range .items[?(@..secretKeyRef)]} {.kind} {.metadata.name} {"\n"}{end}' -A
```

## Control CIS_Controls

TITLE:Encrypt Sensitive Data in Transit CONTROL:v8 3.10 DESCRIPTION:Encrypt sensitive data in transit. Example implementations can include: Transport Layer Security (TLS) and Open Secure Shell (OpenSSH).;TITLE:Encrypt All Sensitive Information in Transit CONTROL:v7 14.4 DESCRIPTION:Encrypt all sensitive information in transit.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-5.4.1 -->

### Rules:

  - secrets_no_environment_variables

### Implementation Status: planned

______________________________________________________________________
