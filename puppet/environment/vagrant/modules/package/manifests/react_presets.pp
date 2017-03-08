###
### react_presets.pp, install necessary webpackages defined in 'package.json'.
###
class package::react_presets {
    include package::nodejs

    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    ## install babelify presets for reactjs (npm)
    exec { 'install-web-packages':
        command => 'npm install --no-bin-links',
        cwd     => "${root_dir}/src/jsx/",
        path    => '/usr/bin',
        require => Class['package::nodejs'],
    }
}