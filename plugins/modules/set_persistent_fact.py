#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: set_persistent_fact
short_description: Records a persistent fact on the destination machine.
description:
  - Uses the M(community.general.ini_file) module to store facts locally.
  - Stores the facts in C(/etc/ansible/facts.d).
  - Fact file will be owned by user and group C(root), with mode C(0640).
author:
    - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
seealso:
- module: community.general.ini_file
options:
  component:
    type: str
    required: true
    description: Used as the filename for the target fact file.
  section:
    type: str
    required: true
    description: Section within the component facts file to store this fact.
  option:
    type: str
    required: true
    description: Name of the fact being stored.
  value:
    type: str
    required: true
    description: Actual fact being stored.
"""

EXAMPLES = """
- name: Record the OpenStack version
  dubzland.utils.set_persistent_fact:
    component: openstack
    section: repository
    option: codename
    value: antelope
"""
