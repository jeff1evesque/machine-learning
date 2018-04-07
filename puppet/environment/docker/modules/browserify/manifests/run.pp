###
### run.pp, ensure browserify service running.
###
class browserify::run {
    ## local variables
    $start_browserify = $::browserify::run

    ## run browserify
    service { 'browserify':
        ensure        => $start_browserify,
        enable        => $start_browserify,
    }
}