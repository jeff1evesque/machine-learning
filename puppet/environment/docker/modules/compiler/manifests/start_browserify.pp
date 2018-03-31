###
### start_browserify.pp, compile jsx into javascript.
###
class compiler::start_browserify {
    include compiler::webcompilers

    ## variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    ## manually compile
    exec { 'browserify':
        command  => "./browserify ${root_dir}",
        cwd      => "${root_puppet}/code/modules/compiler/scripts",
        path     => '/usr/bin',
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}