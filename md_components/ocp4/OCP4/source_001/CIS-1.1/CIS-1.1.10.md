---
x-trestle-comp-def-rules:
  OCP4:
    - name: file_owner_cni_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_cni_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_multus_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_multus_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ip_allocations
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ip_allocations
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_openshift_sdn_cniserver_config
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_openshift_sdn_cniserver_config
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovs_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovs_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovs_conf_db
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovs_conf_db
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovs_sys_id_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovs_sys_id_conf
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovs_conf_db_lock
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovs_conf_db_lock
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovs_vswitchd_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovs_vswitchd_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovsdb_server_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovsdb_server_pid
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovn_cni_server_sock
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovn_cni_server_sock
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_owner_ovn_db_files
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
    - name: file_groupowner_ovn_db_files
      description: Ensure that the Container Network Interface file ownership is set
        to root:root
x-trestle-global:
  profile:
    title: OCP4 CIS Node Profile
    href: profiles/OCP4_CIS_NODE/profile.json
---

# CIS-1.1.10 - \[Master Node Configuration Files\] Ensure that the Container Network Interface file ownership is set to root:root

## Control Statement

Ensure that the Container Network Interface files have ownership set to `root:root`.

## Control rationale_statement

Container Network Interface provides various networking options for overlay networking. You should consult their documentation and restrict their respective file permissions to maintain the integrity of those files. Those files should be owned by `root:root`.

## Control impact_statement

None

## Control remediation_procedure

No remediation required; file permissions are managed by the operator.

## Control audit_procedure

The Cluster Network Operator (CNO) deploys and manages the cluster network components on an OpenShift Container Platform cluster. This includes the Container Network Interface (CNI) default network provider plug-in selected for the cluster during installation. OpenShift Container Platform uses the Multus CNI plug-in to allow chaining of CNI plug-ins. The default Pod network must be configured during cluster installation. By default, the CNO deploys the OpenShift SDN as the default Pod network. 

Ensure that the `multu` and `openshift-sdn` file ownership is set to root:root and the Open vSwitch (OVS) file ownership is set to `openvswitch:openvswitch`. 

The SDN components are deployed as DaemonSets across the master/worker nodes with controllers limited to control plane nodes. OpenShift deploys OVS as a network overlay by default. Various configurations (ConfigMaps and other files managed by the operator via `hostpath` but stored on the container hosts) are stored in the following locations:

CNI:

`/etc/cni/net.d`
`/host/var/run/multus/cni/net.d`

SDN:

`/var/lib/cni/networks/openshift-sdn `
`/var/run/openshift-sdn`

SDN OVS:

`/var/run/openvswitch`
`/etc/openvswitch`
`/run/openvswitch`

Run the following commands.

```

# For CNI multus
for i in $(oc get pods -n openshift-multus -l app=multus -oname); do oc exec -n openshift-multus $i -- /bin/bash -c "stat -c \"%U:%G %n\" /host/etc/cni/net.d/*.conf"; done

for i in $(oc get pods -n openshift-multus -l app=multus -oname); do oc exec -n openshift-multus $i -- /bin/bash -c "stat -c \"%U:%G %n\" /host/var/run/multus/cni/net.d/*.conf"; done

# For SDN pods
for i in $(oc get pods -n openshift-sdn -l app=sdn -oname); do oc exec -n openshift-sdn $i -- find /var/lib/cni/networks/openshift-sdn -type f -exec stat -c \"%U:%G\" {} \;; done

for i in $(oc get pods -n openshift-sdn -l app=sdn -oname); do oc exec -n openshift-sdn $i -- find /var/run/openshift-sdn -type f -exec stat -c %U:%G {} \;; done

# For OVS pods in 4.5
for i in $(oc get pods -n openshift-sdn -l app=ovs -oname); do oc exec -n openshift-sdn $i -- find /var/run/openvswitch -type f -exec stat -c %U:%G {} \;; done 

for i in $(oc get pods -n openshift-sdn -l app=ovs -oname); do oc exec -n openshift-sdn $i -- find /etc/openvswitch -type f -exec stat -c %U:%G {} \;; done 

for i in $(oc get pods -n openshift-sdn -l app=ovs -oname); do oc exec -n openshift-sdn $i -- find /run/openvswitch -type f -exec stat -c %U:%G {} \;; done 

# For OVS pods in 4.6
TBD
```

Verify that the CNI and SDN file ownership is set to `root:root`.

`/host/etc/cni/net.d/00-multus.conf = root:root`
`/host/var/run/multus/cni/net.d/80-openshift-network.conf = root:root`
`/var/lib/cni/networks/openshift-sdn = root:root`
`/var/run/openshift-sdn = root:root`

Verify that the OVS file ownership is set to `openvswitch:openvswitch`.

`/var/run/openvswitch = openvswitch:openvswitch`
`/etc/openvswitch = openvswitch:openvswitch`
`/run/openvswitch = openvswitch:openvswitch`

## Control CIS_Controls

TITLE:Restrict Administrator Privileges to Dedicated Administrator Accounts CONTROL:v8 5.4 DESCRIPTION:Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.;TITLE:Ensure the Use of Dedicated Administrative Accounts CONTROL:v7 4.3 DESCRIPTION:Ensure that all users with administrative account access use a dedicated or secondary account for elevated activities. This account should only be used for administrative activities and not internet browsing, email, or similar activities.;

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: CIS-1.1.10 -->

### Rules:

  - file_owner_cni_conf
  - file_groupowner_cni_conf
  - file_owner_multus_conf
  - file_groupowner_multus_conf
  - file_owner_ip_allocations
  - file_groupowner_ip_allocations
  - file_owner_openshift_sdn_cniserver_config
  - file_groupowner_openshift_sdn_cniserver_config
  - file_owner_ovs_pid
  - file_groupowner_ovs_pid
  - file_owner_ovs_conf_db
  - file_groupowner_ovs_conf_db
  - file_owner_ovs_sys_id_conf
  - file_groupowner_ovs_sys_id_conf
  - file_owner_ovs_conf_db_lock
  - file_groupowner_ovs_conf_db_lock
  - file_owner_ovs_vswitchd_pid
  - file_groupowner_ovs_vswitchd_pid
  - file_owner_ovsdb_server_pid
  - file_groupowner_ovsdb_server_pid
  - file_groupowner_ovn_cni_server_sock
  - file_owner_ovn_cni_server_sock
  - file_owner_ovn_db_files
  - file_groupowner_ovn_db_files

### Implementation Status: planned

______________________________________________________________________
