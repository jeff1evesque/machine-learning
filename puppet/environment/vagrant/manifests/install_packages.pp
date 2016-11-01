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
class general_packages {
    ## set dependency
    require apt
    require install_nodejs
    require system::webcompiler_directory

    ## install packages
    contain package::inotify_tools
    contain package::react_presets
    contain package::jsonschema
    contain package::xmltodict
    contain package::six
    contain package::fetch
    contain package::pyyaml
    contain package::flask_script
    contain package::pytest_flask
    contain package::python_dev
    contain package::libssl_dev
    contain package::scrypt
}

## initiate
include general_packages
