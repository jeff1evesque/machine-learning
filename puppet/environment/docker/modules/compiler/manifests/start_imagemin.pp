###
### start_imagemin.pp, minify images, when possible.
###
class compiler::start_imagemin {
    include compiler::webcompilers

    ## variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    ## manually compile
    exec { 'imagemin':
        command  => "./imagemin ${root_dir}",
        cwd      => "${root_puppet}/code/modules/compiler/scripts",
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}