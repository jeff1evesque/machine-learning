###
### init.pp: install general packages.
###

class package {
    require apt

    ## general packages
    contain package::nodejs
    contain package::inotify_tools
    contain package::react_presets
    contain package::jsonschema
    contain package::xmltodict
    contain package::six
    contain package::fetch
    contain package::pyyaml
    contain package::flask_script
    contain package::pytest_flask
    contain package::libssl_dev
    contain package::scrypt
}
contain package