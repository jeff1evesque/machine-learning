###
### service.pp, ensure nginx running.
###
class nginx::service {
    service { $module::nginx:
        ensure     => running,
        enable     => true,
        hasstatus  => true,
        hasrestart => true,
    }
}
