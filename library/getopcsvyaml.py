#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, canit00 <[email protected]>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Forked & credit to Arvin Amirian for writing the original Python project: https://github.com/arvin-a/openshift-disconnected-operators

from __future__ import print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: getopcsvyaml
short_description: Retrieves Operator CSV YAML & provides related images for later processing.
description:
    - Module takes a local directory path and Operator name to lookup its YAML and provide all related images.
version_added: "2.9"
options:
  src:
    description:
      - The local path to scan.
    required: yes
    type: path
  dest:
    description:
      - The local path to write to.
    required: yes
    type: path
  operator_name:
    description:
      - String used as part of the post *src* when scanning.
    required: yes
    type: str
author:
    - @canit00
'''

RETURN = '''
msg:
    description: Returns image information
    returned: always
    type: list
    ok: [127.0.0.1] => {
    "changed": false,
    "images": [
        "registry.redhat.io/openshift-service-mesh/3scale-istio-adapter-rhel8@sha256:ee8585c2eae863b76e9d4e8e79e3608e642dc3d1ff71a007ef55aa8fe3f11610",
        "registry.redhat.io/openshift-service-mesh/citadel-rhel8@sha256:812b01b38300a2f0e9537c96f48caa22a49b5ddd436230f6ae2742dc91673cfa",
        "registry.redhat.io/openshift-service-mesh/istio-cni-rhel8@sha256:6312d3d5242bd60182a596453d9ccbfe36bf4144b9442bc5871001dbf1231c79",
        "registry.redhat.io/openshift-service-mesh/galley-rhel8@sha256:b8f6562583ce68eb3819f25a43e82e1570173c8374c874d280da81f72dd296f5",
        "registry.redhat.io/openshift-service-mesh/grafana-rhel8@sha256:497bebd338d9c18871482e77e89470ece48d525e027a2d1a4ed971bd525c89cd",
        "registry.redhat.io/openshift-service-mesh/mixer-rhel8@sha256:2fb223a02a72f721acd75311510a954479275605edc9602c04a4f574486fdd6e",
        "registry.redhat.io/openshift-service-mesh/pilot-rhel8@sha256:0622a302ad88755421967733651786c23146c79236e0801f837c692eb14ad6b9",
        "registry.redhat.io/openshift-service-mesh/prometheus-rhel8@sha256:6c32e8db039dd06429a0e71919e7d2b914baf8e28d35ca17e6c9e40179a0871f",
        "registry.redhat.io/openshift-service-mesh/proxy-init-rhel7@sha256:f965d1eb6e9139bfbf55b8e14fcd5cb28619cd89b6576b45aa33ae6211bc0963",
        "registry.redhat.io/openshift-service-mesh/proxyv2-rhel8@sha256:6f8df84d1c20842ec1c31fd3171de8f4601b2a99ab77bae93c242763772971b7",
        "registry.redhat.io/openshift-service-mesh/sidecar-injector-rhel8@sha256:baee6083db8c87d66035b3297b075e00c01b31b6701c25ec72ca438553e923dc",
        "registry.redhat.io/openshift-service-mesh/citadel-rhel8@sha256:8dfed5010965acb17c7e69dd7fe8bf02306cdfa5fcb2a47b589eb5a9d07513db",
        "registry.redhat.io/openshift-service-mesh/istio-cni-rhel8@sha256:994e3f13a489af11cf3c76d3596268e0e62118127e618899aecbcc48fbc271b5",
        "registry.redhat.io/openshift-service-mesh/galley-rhel8@sha256:69eac8be8d5e4f4e991915d0dcde44d91409c375bf760ea37061b1c1d091ab9c",
        "registry.redhat.io/openshift-service-mesh/grafana-rhel8@sha256:c67d317b2ef696fc67be7c617cc5788047b681d09346da81f8a6e79ebea89573",
        "registry.redhat.io/openshift-service-mesh/ior-rhel8@sha256:5b12b568b8da4539b11ce6cd8cea7d7b34da8112e6857a3ad562bf7281d5cb90",
        "registry.redhat.io/openshift-service-mesh/mixer-rhel8@sha256:7f4b39c47ffd49881420ca560086ae757dec152c8b80fe63bbbeb89bedb71ca6",
        "registry.redhat.io/openshift-service-mesh/pilot-rhel8@sha256:367d300abe577313899bb4a139e1e1de6c496a4a009bf2c4545b6113e0d95419",
        "registry.redhat.io/openshift-service-mesh/prometheus-rhel8@sha256:1b70dfedb073936b2bc900b632917a6c2c8e27efcf94d526e1834295a34edfb7",
        "registry.redhat.io/openshift-service-mesh/proxy-init-rhel7@sha256:51f4ca947829c20f3882e779e6858af6bce39b6c0b00b5603c7b76dac289bfb4",
        "registry.redhat.io/openshift-service-mesh/proxyv2-rhel8@sha256:3a2b2eb7d38498319661f5d9f1c484512e154cac07185cafc27b533fb59693c3",
        "registry.redhat.io/openshift-service-mesh/sidecar-injector-rhel8@sha256:3d5715fb1e9facb9a7a06869cb6d7992708825959982e1782b30d71f917001b4"
    ],
    "invocation": {
        "module_args": {
            "dest": "/tmp/ansible.zgm3dutocontent",
            "operator_name": "servicemeshoperator",
            "src": "/tmp/ansible.7s73ltrxmanifest"
        }
    }
}

'''

EXAMPLES = '''
- name: Get Operator CsvYaml
  getopcsvyaml:
    src: "{{manifest_root_dir}}"
    dest: "{{content_root_dir}}"
    operator_name: "{{ item.package.split('/')[1] }}"

- name: Get Operator CsvYaml
  getopcsvyaml:
    src: "{{manifest_root_dir}}"
    dest: "{{content_root_dir}}"
    operator_name: "{{item.item.name.split('/')[1]}}"
'''
import os
import glob
import yaml
from jinja2 import Template
from pathlib import Path
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes, to_native, to_text

operator_image_list = []
rc = None
out = ''
err = ''

def main():
    result = dict(
        changed=False,
        images = ''
    )

    module = AnsibleModule(
        argument_spec=dict(
            operator_name=dict(type='str', required=True),
            src=dict(type='str', required=True),
            dest=dict(type='str', required=True)
        )
    )

    params = module.params
    manifest_root_dir = params['src']
    content_root_dir = params['dest']
    operator_name = params['operator_name']

    operatorCsvYaml = getOperatorCsvYaml(operator_name, manifest_root_dir)
    extractRelatedImagesToFile(operatorCsvYaml)
    result['images'] = operator_image_list
    writeImageList2Disk(operator_image_list, content_root_dir)
    module.exit_json(**result)

def getOperatorCsvYaml(operator_name, manifest_root_dir):
  try:
    # Find manifest file
    operatorPackagePath = glob.glob(
        os.path.join(
            manifest_root_dir,
            operator_name + '*',
            '*package*'))
    operatorManifestPath = os.path.dirname(operatorPackagePath[0])
    operatorPackageFilename = operatorPackagePath[0]

    with open(operatorPackageFilename, 'r') as packageYamlFile:
      packageYaml = yaml.safe_load(packageYamlFile)
      default = packageYaml['defaultChannel']
      for channel in packageYaml['channels']:
        if channel['name'] == default:
          currentChannel = channel['currentCSV']
          csvFilePath = GetOperatorCsvPath(
              operatorManifestPath, currentChannel)
          with open(str(csvFilePath)) as yamlFile:
          #with open(str(csvFilePath, 'r')) as yamlFile:
            csvYaml = yaml.safe_load(yamlFile)
            return csvYaml
  except (yaml.YAMLError, IOError) as exc:
    module.fail_json(failed=True, msg="%s" % to_native(exc))
  return None

# Search within manifest folder for correct CSV
def GetOperatorCsvPath(search_path, search_string):
  yamlFiles = Path(search_path).glob("*/**/*.yaml")
  for fileName in yamlFiles:
    #with open(fileName) as f:
    with (fileName).open() as f:
      if search_string in f.read():
        return fileName

# Get a non duplicate list of images to download
def getImages():
  return operator_image_list

# Add image to a list of images to download
def setImages(image):
  if image not in operator_image_list:
    operator_image_list.append(image)

# Write related images from an operator CSV YAML to a file for later processing
def extractRelatedImagesToFile(operatorCsvYaml):
  for entry in operatorCsvYaml['spec']['relatedImages']:
    if('image' in entry):
      setImages(entry['image'])
    elif('value' in entry):
      setImages(entry['value'])

def writeImageList2Disk(operator_image_list, content_root_dir):
  imglist = os.path.join(content_root_dir, 'images.txt')
  for image in operator_image_list:
    with open(imglist, "a+") as il:
      il.write(image + '\n')

if __name__ == '__main__':
    main()
