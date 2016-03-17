### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::react_presets {
    ## install babelify presets for reactjs (npm)
    exec { 'install-babelify-presets':
        command     => 'npm install --no-bin-links',
        cwd         => '/vagrant/src/jsx/',
        path        => '/usr/bin',
    }
}