### install_packages.pp: install general packages.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## general packages
include apt
include package::dos2unix
include package::inotify_tools
include package::react_presets
include package::jsonschema
include package::xmltodict
include package::six
include system::webcompiler_directories

## nodejs, with npm: this cannot be wrapped into a module, and included, as
#      needed. Puppet will only allow one instance of this class, regardless of
#      of its implementation.
class { 'nodejs':
  repo_url_suffix => '5.x',
}