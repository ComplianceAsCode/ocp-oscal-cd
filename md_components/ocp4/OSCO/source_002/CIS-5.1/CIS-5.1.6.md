---
x-trestle-comp-def-rules:
  OSCO:
    - name: accounts_restrict_service_account_tokens
      description: Ensure that Service Account Tokens are only mounted where necessary
        (info)
x-trestle-global:
  profile:
    title: OCP4 CIS Profile
    href: profiles/OCP4_CIS/profile.json
---

# CIS-5.1.6 - \[RBAC and Service Accounts\] Ensure that Service Account Tokens are only mounted where necessary

## Control Statement

Service accounts tokens should not be mounted in pods except where the workload running in the pod explicitly needs to communicate with the API server

## Control rationale_statement

Mounting service account tokens inside pods can provide an avenue for privilege escalation attacks where an attacker is able to compromise a single pod in the cluster.

Avoiding mounting these tokens removes this attack avenue.

## Control impact_statement

Pods mounted without service account tokens will not be able to communicate with the API server, except where the resource is available to unauthenticated principals.

## Control remediation_procedure

Modify the definition of pods and service accounts which do not need to mount service account tokens to disable it.

## Control audit_procedure

Review pod and service account objects in the cluster and ensure that the option below is set, unless the resource explicitly requires this access.

```
automountServiceAccountToken: false
```

## Control CIS_Controls

TITLE:Only Allow Access to Authorized Cloud Storage or Email Providers CONTROL:v7 13.4 DESCRIPTION:Only allow access to authorized cloud storage or email providers.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-5.1.6 -->

### Rules:

  - accounts_restrict_service_account_tokens

### Implementation Status: planned

______________________________________________________________________
