###
### run.pp, ensure uglifyjs service running.
###
class uglifyjs::run {
    ## local variables
    $start_uglifyjs = $::uglifyjs::run

    ## run uglifyjs
    service { 'uglifyjs':
        ensure      => $start_uglifyjs,
        enable      => $start_uglifyjs,
    }
}