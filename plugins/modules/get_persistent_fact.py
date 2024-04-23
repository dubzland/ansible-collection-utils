#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: get_persistent_fact
short_description: Retrieves a fact from local facts.
description:
  - Reads the fact from variables in C(hostvars['ansible_local']), so be sure
    facts are already gathered.
  - Uses the M(ansible.builtin.set_fact) module to actually assign the fact.
author:
    - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
seealso:
- module: ansible.builtin.set_fact
options:
  component:
    type: str
    required: true
    description: Section within C(hostvars['ansible_local']) containing the fact.
  section:
    type: str
    required: true
    description: Section within the component facts file where fact is stored.
  option:
    type: str
    required: true
    description: Name of the fact being retrieved.
  as:
    type: str
    required: true
    description: Variable to be set with the fact value.
"""

EXAMPLES = """
- name: Retrieve the OpenStack version
  dubzland.utils.get_persistent_fact:
    component: openstack
    section: repository
    option: codename
    as: _openstack_version
"""
