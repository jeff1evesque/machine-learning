###
### service.pp, ensure nginx running.
###
class reverse_proxy::service {
    service { $reverse_proxy::nginx:
        ensure     => $reverse_proxy::run,
        enable     => $reverse_proxy::run,
        hasstatus  => true,
        hasrestart => true,
    }
}
