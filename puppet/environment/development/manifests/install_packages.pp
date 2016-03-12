### install_packages.pp: install general packages.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

include apt
include package::dos2unix
include package::inotify_tools
include package::nodejs
include package::react_presets
include package::jsonschema
include package::xmltodict
include package::six
include system::webcompiler_directories