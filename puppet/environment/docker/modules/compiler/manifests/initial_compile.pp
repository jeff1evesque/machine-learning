###
### initial_compile.pp, manually compile javascript.
###
class compiler::initial_compile {
    include package::package_json
    include package::webcompilers

    ## local variables
    $hiera       = lookup('general')
    $root_dir    = $hiera['root']
    $root_puppet = $hiera['root_puppet']

    $sources  = [
        'jsx',
        'img',
        'scss'
    ]

    ## manually compile jsx asset, since first pass through via
    ## 'start_uglifyjs.pp' does not have adequate scope resolution.
    exec { 'rerun-uglifyjs':
        command  => "./uglifyjs ${root_dir}",
        cwd      => "${root_puppet}/code/modules/compiler/scripts",
        path     => '/usr/bin',
        provider => shell,
        require => [
            Class['package::webcompilers'],
            Class['package::package_json'],
        ],
    }
}