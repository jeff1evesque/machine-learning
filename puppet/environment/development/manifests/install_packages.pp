### install_packages.pp: install general packages.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## nodejs, with npm: this cannot be wrapped into a module, and included, as
#      needed. Puppet will only allow one instance of this class, regardless of
#      of its implementation.
class install_nodejs {
    ## set dependency
    require apt

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => '5.x',
    }
    contain nodejs
}

## general packages
class install_general_packages {
    ## set dependency
    require apt
    require install_nodejs

    ## install packages
    include package::dos2unix
    include package::inotify_tools
    include package::react_presets
    include package::jsonschema
    include package::xmltodict
    include package::six
    include system::webcompiler_directories
}

## constructor
class constructor {
    contain install_nodejs
    contain install_general_packages
}
include constructor