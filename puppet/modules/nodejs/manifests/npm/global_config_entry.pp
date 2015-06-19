# See README.md for usage information.
define nodejs::npm::global_config_entry (
  $ensure         = 'present',
  $config_setting = $title,
  $npm_path       = $::nodejs::params::npm_path,
  $value          = undef,
) {

  validate_re($ensure, '^(present|absent)$', "${module_name}::npm::global_config_entry : Ensure parameter must be present or absent")

  $command = $ensure ? {
    'absent' => "config delete ${config_setting}",
    default  => "config set ${config_setting} ${value} --global",
  }

  exec { "npm_config ${ensure} ${title}":
    command => "${npm_path} ${command}",
  }
}
