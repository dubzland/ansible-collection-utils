# Ansible Collection: Utils

[![Gitlab pipeline status (self-hosted)](https://git.dubzland.com/dubzland/ansible-collections/utils/badges/main/pipeline.svg)](https://git.dubzland.com/dubzland/ansible-collections/utils/pipelines?scope=all&page=1&ref=main)
[![Ansible Galaxy](https://img.shields.io/badge/dynamic/json?style=flat&label=galaxy&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/dubzland/utils/&query=highest_version.version)](https://galaxy.ansible.com/ui/repo/published/dubzland/utils/)
[![Liberapay patrons](https://img.shields.io/liberapay/patrons/jdubz)](https://liberapay.com/jdubz/donate)
[![Liberapay receiving](https://img.shields.io/liberapay/receives/jdubz)](https://liberapay.com/jdubz/donate)

General purpose utilities for Ansible roles and collections.

## Ansible version compatibility

This collection has been tested against following ansible-core versions:

- 2.14
- 2.15
- 2.16

Also tested against the current development version of `ansible-core`.

## Included content

### Modules

| Name                                                      | Description                                    |
| --------------------------------------------------------- | ---------------------------------------------- |
| [dubzland.utils.get_persistent_fact][get_persistent_fact] | Retrieves facts stored as ansible custom facts |
| [dubzland.utils.set_persistent_fact][set_persistent_fact] | Stores facts in ansible custom facts           |

## Licensing

This collection is primarily licensed and distributed as a whole under the GPLv3 License.

See [COPYING](COPYING) for the full text.

## Author

- [Josh Williams](https://dubzland.com)

[get_persistent_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/utils/get_persistent_fact_module.html
[set_persistent_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/utils/set_persistent_fact_module.html
