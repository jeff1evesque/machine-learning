###
### start_sass.pp, minify scss into css.
###
class compiler::start_sass {
    include compiler::webcompilers

    ## variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    ## manually compile: increase default timeout (300s)
    exec { 'sass':
        command  => "./sass ${root_dir}",
        cwd      => "${root_puppet}/code/modules/compiler/scripts",
        timeout  => 700,
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}