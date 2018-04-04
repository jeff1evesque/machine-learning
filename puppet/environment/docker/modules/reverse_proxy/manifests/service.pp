###
### service.pp, ensure nginx running.
###
class reverse_proxy::service {
    ## local variables
    $reverse_proxy_service = $::reverse_proxy::nginx
    $reverse_proxy_start   = $::reverse_proxy::run

    ## ensure service
    service { $reverse_proxy_service:
        ensure     => $reverse_proxy_start,
        enable     => $reverse_proxy_start,
        hasstatus  => true,
        hasrestart => true,
    }
}
