# PRIVATE CLASS: Do not use directly
class nodejs::repo::nodesource {
  $enable_src     = $nodejs::repo_enable_src
  $ensure         = $nodejs::repo_ensure
  $pin            = $nodejs::repo_pin
  $priority       = $nodejs::repo_priority
  $proxy          = $nodejs::repo_proxy
  $proxy_password = $nodejs::repo_proxy_password
  $proxy_username = $nodejs::repo_proxy_username
  $url_suffix     = $nodejs::repo_url_suffix

  case $::osfamily {
    'RedHat': {
      if $::operatingsystemrelease =~ /^5\.(\d+)/ {
        include ::epel
        $dist_version  = '5'
        $name_string   = 'Enterprise Linux 5'
      }

      elsif $::operatingsystemrelease =~ /^6\.(\d+)/ {
        $dist_version = '6'
        $name_string  = 'Enterprise Linux 6'
      }

      elsif $::operatingsystemrelease =~ /^7\.(\d+)/ {
        $dist_version = '7'
        $name_string  = 'Enterprise Linux 7'
      }

      # Fedora
      elsif $::operatingsystemrelease =~ /(19)|2[01]/ {
        $dist_version  = $::operatingsystemrelease
        $name_string   = "Fedora Core ${::operatingsystemrelease}"
      }

      else {
        fail("Could not determine NodeSource repository URL for operatingsystem: ${::operatingsystem} operatingsystemrelease: ${::operatingsystemrelease}.")
      }

      $dist_type = $::operatingsystem ? {
        'Fedora' => 'fc',
        default  => 'el',
      }

      # nodesource repo
      $descr   = "Node.js Packages for ${name_string} - \$basearch"
      $baseurl = "https://rpm.nodesource.com/pub/${dist_type}/${dist_version}/\$basearch"

      # nodesource-source repo
      $source_descr   = "Node.js for ${name_string} - \$basearch - Source"
      $source_baseurl = "https://rpm.nodesource.com/pub/${dist_type}/${dist_version}/SRPMS"

      class { '::nodejs::repo::nodesource::yum': }
      contain '::nodejs::repo::nodesource::yum'

      if $::operatingsystemrelease =~ /^5\.(\d+)/ {
        # On EL 5, EPEL needs to be applied first
        Class['::epel'] -> Class['::nodejs::repo::nodesource::yum']
      }

    }
    'Linux': {
      if $::operatingsystem == 'Amazon' {

        # Recent Amazon Linux instances
        if $::operatingsystemrelease =~ /^201[4-9]\./ {
          $dist_type    = 'el'
          $dist_version = '7'
          $name_string  = 'Enterprise Linux 7'
        }
        else {
          $dist_type    = 'el'
          $dist_version = '6'
          $name_string  = 'Enterprise Linux 6'
        }

        # nodesource repo
        $descr   = "Node.js Packages for ${name_string} - \$basearch"
        $baseurl = "https://rpm.nodesource.com/pub/${dist_type}/${dist_version}/\$basearch"

        # nodesource-source repo
        $source_descr   = "Node.js for ${name_string} - \$basearch - Source"
        $source_baseurl = "https://rpm.nodesource.com/pub/${dist_type}/${dist_version}/SRPMS"

        class { '::nodejs::repo::nodesource::yum': }
        contain '::nodejs::repo::nodesource::yum'
      }

      else {
        if ($ensure == 'present') {
          fail("Unsupported managed NodeSource repository for operatingsystem: ${::operatingsystem}.")
        }
      }
    }
    'Debian': {
      class { '::nodejs::repo::nodesource::apt': }
      contain '::nodejs::repo::nodesource::apt'
    }
    default: {
      if ($ensure == 'present') {
        fail("Unsupported managed NodeSource repository for osfamily: ${::osfamily}, operatingsystem: ${::operatingsystem}.")
      }
    }
  }
}
