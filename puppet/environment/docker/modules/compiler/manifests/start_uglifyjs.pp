###
### start_uglifyjs.pp, minify javascript.
###
class compiler::start_uglifyjs {
    include compiler::webcompilers

    ## variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    ## manually compile
    exec { 'uglifyjs':
        command  => "./uglifyjs ${root_dir}",
        cwd      => "${root_puppet}/code/modules/compiler/scripts",
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}