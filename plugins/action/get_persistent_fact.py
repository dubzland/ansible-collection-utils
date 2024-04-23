# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def get_value(self, component, section, option, vars):
        if "ansible_local" not in vars:
            raise AnsibleActionFail("'ansible_local' not populated")

        ansible_local = vars["ansible_local"]

        if component not in ansible_local:
            raise AnsibleActionFail(
                "%s vars not set in ansible_local. Did you gather facts?" % component
            )

        component_facts = ansible_local[component]

        keys = [section, option]
        _element = component_facts
        for key in keys:
            if key in _element:
                _element = _element[key]
            else:
                raise AnsibleActionFail(
                    "Unable to find %s fact: %s -> %s" % (component, section, option)
                )

        return _element

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp

        component = self._task.args["component"]
        section = self._task.args["section"]
        option = self._task.args["option"]
        fact_name = self._task.args["as"]
        new_task = self._task.copy()

        new_task.args = dict()
        new_task.args[fact_name] = self.get_value(component, section, option, task_vars)

        # Execute the builtin set_fact
        set_fact_action = self._shared_loader_obj.action_loader.get(
            "ansible.builtin.set_fact",
            task=new_task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )

        result.update(set_fact_action.run(task_vars=task_vars))

        return result
