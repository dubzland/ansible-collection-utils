# Ansible Collection: Utils

[![Gitlab pipeline][pipeline-badge]][pipeline-url]
[![Gitlab coverage][coverage-badge]][coverage-url]
[![Galaxy Version][galaxy-badge]][galaxy-url]
[![license][license-badge]][license-url]
[![Liberapay patrons][liberapay-patrons-badge]][liberapay-url]
[![Liberapay receiving][liberapay-receives-badge]][liberapay-url]

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

[pipeline-badge]: https://img.shields.io/gitlab/pipeline-status/dubzland%2Fansible-collections%2Futils?gitlab_url=https%3A%2F%2Fgit.dubzland.com&branch=main&style=flat-square&logo=gitlab
[pipeline-url]: https://git.dubzland.com/dubzland/ansible-collections/utils/pipelines?scope=all&page=1&ref=main
[coverage-badge]: https://img.shields.io/gitlab/pipeline-coverage/dubzland%2Fansible-collections%2Futils?gitlab_url=https%3A%2F%2Fgit.dubzland.com&branch=main&style=flat-square&logo=gitlab
[coverage-url]: https://git.dubzland.com/dubzland/ansible-collections/utils/pipelines?scope=all&page=1&ref=main
[galaxy-badge]: https://img.shields.io/badge/dynamic/json?style=flat-square&label=galaxy&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/dubzland/utils/&query=highest_version.version
[galaxy-url]: https://galaxy.ansible.com/ui/repo/published/dubzland/utils/
[license-badge]: https://img.shields.io/gitlab/license/dubzland%2Fcontainer-images%2Fci-python?gitlab_url=https%3A%2F%2Fgit.dubzland.com&style=flat-square
[license-url]: https://git.dubzland.com/dubzland/container-images/ci-python/-/blob/main/LICENSE
[liberapay-patrons-badge]: https://img.shields.io/liberapay/patrons/jdubz?style=flat-square&logo=liberapay
[liberapay-receives-badge]: https://img.shields.io/liberapay/receives/jdubz?style=flat-square&logo=liberapay
[liberapay-url]: https://liberapay.com/jdubz/donate
[get_persistent_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/utils/get_persistent_fact_module.html
[set_persistent_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/utils/set_persistent_fact_module.html
