###
### service.pp, ensure nginx running.
###
class nginx::service {
    service { $nginx::nginx:
        ensure     => $nginx::run,
        enable     => $nginx::run,
        hasstatus  => true,
        hasrestart => true,
    }
}
