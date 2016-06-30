### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_uglifyjs {
    # variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run uglifyjs
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'uglifyjs':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # local variables
        $asset_dir = "${root_dir}/interface/static/js"
        $src_dir   = "${root_dir}/src/js"

        # manually compile
        exec { 'uglifyjs':
            command  => "for file in $asset_dir/*; do uglifyjs -c --output $root_dir/interface/static/js/\${file%.*}.min.js $src_dir/$file; done",
            provider => shell,
            path     => '/usr/bin',
        }
    }
}