### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::react_presets {
    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    ## install babelify presets for reactjs (npm)
    exec { 'install-babelify-presets':
        command => 'npm install --no-bin-links',
        cwd     => "${root_dir}/src/jsx/",
        path    => '/usr/bin',
    }
}