###
### run.pp, ensure sass service running.
###
class sass::run {
    ## local variables
    $root_dir     = $::sass::root_dir
    $start_sass   = $::sass::run
    $root_puppet  = $::sass::root_puppet
    $compiler_dir = "${root_puppet}/code/modules/sass/scripts"

    ## run sass
    if $start_sass {
        exec { 'start-sass':
            command => "./sass ${root_dir}",
            path    => '/usr/bin',
            cwd     => $compiler_dir,
            unless  => 'pgrep node-sass',
        }
    }
}