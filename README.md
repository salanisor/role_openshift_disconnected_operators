Role Name
=========

# OpenShift Offline Operator Catalog Build and Mirror

This Ansible role will create a custom operator catalogue based on the desired operators and mirror the images to a local registry.

Why create this?

Because the current catalog build and mirror (https://docs.openshift.com/container-platform/4.5/operators/olm-restricted-networks.html) takes 1-5 hours to create and more than 50% of the catalog is not usable offline anyways. This tool allows you to create a custom catalog with only the operators you need.

## Requirements

This tool was tested with the following versions of the runtime and utilities.

1. RHEL 7.8, Centos 8
2. Python 3.7.6 (with pyyaml,jinja2,jmespath library)
3. Podman v1.8 (If you use anything below 1.8, you might run into issues with multi-arch manifests)
4. Skopeo 0.1.41

Please note this only works with operators that meet the following criterea

1. Have a CSV in the manifest that contains a full list of related images
2. The related images are tagged with a SHA

For a full list of operators that work offline please see link below
<https://access.redhat.com/articles/4740011>

Role Variables
--------------

See all possible [variables](docs/examples/vars.yml) & how-to.

Dependencies
------------

You can obtain the pull secret for quay.io and registry.redhat.io from the [Pull-secret-page](https://cloud.redhat.com/openshift/install/pull-secret)

Example Playbook
----------------

Run playbook: `ansible-playbook -vvv pb_ocp_disconnected_operators.yaml --ask-vault-pass`

    ---
    - hosts: bastion
      gather_facts: true
      pre_tasks:
      - include_tasks: pre_tasks.yaml
      roles:
      - role: role_openshift_disconnected_operators

License
-------

BSD

Author Information
------------------
@canit00

Project forked from [Arvin Amirian](https://github.com/arvin-a/openshift-disconnected-operators)
