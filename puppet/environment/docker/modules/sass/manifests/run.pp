###
### run.pp, ensure sass service running.
###
class sass::run {
    ## local variables
    $start_sass = $::sass::run

    ## run sass
    service { 'sass':
        ensure  => $start_sass,
        enable  => $start_sass,
    }
}