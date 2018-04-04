###
### service.pp, ensure nginx running.
###
class reverse_proxy::service {
    ## local variables
    $reverse_proxy_start = $::reverse_proxy::run

    ## ensure service
    service { 'nginx':
        ensure     => $reverse_proxy_start,
        enable     => $reverse_proxy_start,
        hasstatus  => true,
        hasrestart => true,
    }
}
