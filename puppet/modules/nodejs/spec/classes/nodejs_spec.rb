require 'spec_helper'

describe 'nodejs', :type => :class do

  context 'when run on Debian Squeeze' do
    let :facts do
      {
        :osfamily               => 'Debian',
        :operatingsystemrelease => '6.0.10',
      }
    end

    it 'should fail' do
      expect { catalogue }.to raise_error(Puppet::Error, /The nodejs module is not supported on Debian Squeeze./)
    end
  end

 [ '7.0', '8.0', '10.04', '12.04', '14.04', ].each do |operatingsystemrelease|

    if operatingsystemrelease =~ /^[78]\.(\d+)/
      lsbdistid       = 'Debian'
      operatingsystem = 'Debian'
    else
      lsbdistid       = 'Ubuntu'
      operatingsystem = 'Ubuntu'
    end

    if operatingsystemrelease == '7.0'
      lsbdistcodename = 'Wheezy'
    elsif operatingsystemrelease == '8.0'
      lsbdistcodename = 'Jessie'
    elsif operatingsystemrelease == '10.04'
      lsbdistcodename = 'Lucid'
    elsif operatingsystemrelease == '12.04'
      lsbdistcodename = 'Precise'
    else
      lsbdistcodename = 'Trusty'
    end
    
    context "when run on #{lsbdistid} release #{operatingsystemrelease}" do
    
      let :facts do
        {
          :lsbdistcodename        => lsbdistcodename,
          :lsbdistid              => lsbdistid,
          :operatingsystem        => operatingsystem,
          :operatingsystemrelease => operatingsystemrelease,
          :osfamily               => 'Debian',
        }
      end

      # legacy_debian_symlinks
      context 'with legacy_debian_symlinks set to true' do
        let (:params) { { :legacy_debian_symlinks => true,} }

        it 'the file resource /usr/bin/node should be in the catalog' do
          should contain_file('/usr/bin/node')
        end
        it 'the file resource /usr/share/man/man1/node.1.gz should be in the catalog' do
          should contain_file('/usr/share/man/man1/node.1.gz')
        end
      end

      context 'with legacy_debian_symlinks set to false' do
        let (:params) { { :legacy_debian_symlinks => false,} }
      
        it 'the file resource /usr/bin/node should not be in the catalog' do
          should_not contain_file('/usr/bin/node')
        end
        it 'the file resource /usr/share/man/man1/node.1.gz should not be in the catalog' do
          should_not contain_file('/usr/share/man/man1/node.1.gz')
        end
      end

      # manage_package_repo
      context 'with manage_package_repo set to true' do
        let (:default_params) { { :manage_package_repo => true,} }

        context 'and repo_class set to ::nodejs::repo::nodesource' do
          let :params do
            default_params.merge!({
              :repo_class => 'nodejs::repo::nodesource',
            })
          end

          it '::nodejs::repo::nodesource should be in the catalog' do
            should contain_class('nodejs::repo::nodesource')
          end

          it '::nodejs::repo::nodesource::apt should be in the catalog' do
            should contain_class('nodejs::repo::nodesource::apt')
          end
        end

        context 'and repo_enable_src set to true' do
          let :params do
            default_params.merge!({
              :repo_enable_src => true,
            })
          end

          it 'the repo apt::source resource should contain include_src = true' do
            should contain_apt__source('nodesource').with({
              'include_src' => true,
            })
          end
        end

        context 'and repo_enable_src set to false' do
          let :params do
            default_params.merge!({
              :repo_enable_src => false,
            })
          end

          it 'the repo apt::source resource should contain include_src = false' do
            should contain_apt__source('nodesource').with({
              'include_src' => false,
            })
          end
        end

        context 'and repo_pin set to 10' do
          let :params do
            default_params.merge!({
              :repo_pin => '10',
            })
          end

          it 'the repo apt::source resource should contain pin = 10' do
            should contain_apt__source('nodesource').with({
              'pin' => '10'
            })
          end
        end

        context 'and repo_pin not set' do
          let :params do
            default_params.merge!({
              :repo_pin => 'false',
            })
          end

          it 'the repo apt::source resource should contain pin = false' do
            should contain_apt__source('nodesource').with({
              'pin' => 'false'
            })
          end
        end

        context 'and repo_url_suffix set to node_0.12' do
          let :params do
            default_params.merge!({
              :repo_url_suffix => 'node_0.12',
            })
          end

          it 'the repo apt::source resource should contain location = https://deb.nodesource.com/node_0.12' do
            should contain_apt__source('nodesource').with({
              'location' => 'https://deb.nodesource.com/node_0.12'
            })
          end
        end

        context 'and repo_ensure set to present' do
          let :params do
            default_params.merge!({
              :repo_ensure => 'present',
            })
          end

          it 'the nodesource apt sources file should exist' do
            should contain_apt__source('nodesource')
          end
        end

        context 'and repo_ensure set to absent' do
          let :params do
            default_params.merge!({
              :repo_ensure => 'absent',
            })
          end

          it 'the nodesource apt sources file should not exist' do
            should contain_apt__source('nodesource').with({
              'ensure' => 'absent',
            }) 
          end
        end
      end

      context 'with manage_package_repo set to false' do
        let (:params) {{
          :manage_package_repo => false,
        }}

        it '::nodejs::repo::nodesource should not be in the catalog' do
          should_not contain_class('::nodejs::repo::nodesource')
        end
      end

      # nodejs_debug_package_ensure
      context 'with nodejs_debug_package_ensure set to present' do
        let (:params) { { :nodejs_debug_package_ensure => 'present',} }

        it 'the nodejs package with debugging symbols should be installed' do
          should contain_package('nodejs-dbg').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with nodejs_debug_package_ensure set to absent' do
        let (:params) { { :nodejs_debug_package_ensure => 'absent',} }

        it 'the nodejs package with debugging symbols should not be present' do
          should contain_package('nodejs-dbg').with({
            'ensure' => 'absent',
          })
        end
      end

      # nodejs_dev_package_ensure
      context 'with nodejs_dev_package_ensure set to present' do
        let (:params) { { :nodejs_dev_package_ensure => 'present',} }

        if operatingsystemrelease == '10.04' or operatingsystemrelease == '7.0'
          it 'the nodejs development package resource should not be present' do
            should_not contain_package('nodejs-dev')
          end
        else
          it 'the nodejs development package should be installed' do
            should contain_package('nodejs-dev').with({
              'ensure' => 'present',
            })
          end
        end
      end

      context 'with nodejs_dev_package_ensure set to absent' do
        let (:params) { { :nodejs_dev_package_ensure => 'absent',} }

        if operatingsystemrelease =~ /^(7\.0)|(10\.04)/
          it 'the nodejs development package resource should not be present' do
            should_not contain_package('nodejs-dev')
          end
        else
          it 'the nodejs development package should not be present' do
            should contain_package('nodejs-dev').with({
              'ensure' => 'absent',
            })
          end
        end
      end

      # nodejs_package_ensure
      context 'with nodejs_package_ensure set to present' do
        let (:params) { { :nodejs_package_ensure => 'present',} }

        it 'the nodejs package should be present' do
          should contain_package('nodejs').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with nodejs_package_ensure set to absent' do
        let (:params) { { :nodejs_package_ensure => 'absent',} }

        it 'the nodejs package should be absent' do
          should contain_package('nodejs').with({
            'ensure' => 'absent',
          })
        end
      end

      # npm_package_ensure
      context 'with npm_package_ensure set to present' do
        let (:params) { { :npm_package_ensure => 'present',} }

        if operatingsystemrelease =~ /^(7\.0)|(10\.04)/
          it 'the npm package resource should not be present' do
            should_not contain_package('npm')
          end
        else
          it 'the npm package should be present' do
            should contain_package('npm').with({
              'ensure' => 'present',
            })
          end
        end
      end

      context 'with npm_package_ensure set to absent' do
        let (:params) { { :nodejs_package_ensure => 'absent',} }

        if operatingsystemrelease =~ /^(7\.0)|(10\.04)/
          it 'the npm package resource should not be present' do
            should_not contain_package('npm')
          end
        else
          it 'the npm package should be absent' do
            should contain_package('npm').with({
              'ensure' => 'absent',
            })
          end
        end
      end

    end
  end

  context 'when run on Fedora 18' do
    let :facts do
      {
        :osfamily               => 'RedHat',
        :operatingsystem        => 'Fedora',
        :operatingsystemrelease => '18',
      }
    end

    it do
      expect { catalogue }.to raise_error(Puppet::Error, /The nodejs module is not supported on Fedora 18./)
    end
  end

  [ '5.0', '6.0', '7.0', '20', '21' ].each do |operatingsystemrelease|

    osversions = operatingsystemrelease.split('.')
    operatingsystemmajrelease = osversions[0]

    if operatingsystemrelease =~ /^[5-7]\.(\d+)/
      operatingsystem     = 'CentOS'
      repo_baseurl        = "https://rpm.nodesource.com/pub/el/#{operatingsystemmajrelease}/\$basearch"
      repo_source_baseurl = "https://rpm.nodesource.com/pub/el/#{operatingsystemmajrelease}/SRPMS"
      repo_descr          = "Node.js Packages for Enterprise Linux #{operatingsystemmajrelease} - \$basearch"
      repo_source_descr   = "Node.js for Enterprise Linux #{operatingsystemmajrelease} - \$basearch - Source"
    else
      operatingsystem     = 'Fedora'
      repo_baseurl        = "https://rpm.nodesource.com/pub/fc/#{operatingsystemmajrelease}/\$basearch"
      repo_source_baseurl = "https://rpm.nodesource.com/pub/fc/#{operatingsystemmajrelease}/SRPMS"
      repo_descr          = "Node.js Packages for Fedora Core #{operatingsystemmajrelease} - \$basearch"
      repo_source_descr   = "Node.js for Fedora Core #{operatingsystemmajrelease} - \$basearch - Source"
    end

    context "when run on #{operatingsystem} release #{operatingsystemrelease}" do
    
      let :facts do
        {
          :operatingsystem           => operatingsystem,
          :operatingsystemmajrelease => operatingsystemmajrelease,
          :operatingsystemrelease    => operatingsystemrelease,
          :osfamily                  => 'RedHat',
        }
      end

      # manage_package_repo
      context 'with manage_package_repo set to true' do
        let (:default_params) { { :manage_package_repo => true,} }

        context 'and repo_class set to ::nodejs::repo::nodesource' do
          let :params do
            default_params.merge!({
              :repo_class => 'nodejs::repo::nodesource',
            })
          end

          it '::nodejs::repo::nodesource should be in the catalog' do
            should contain_class('nodejs::repo::nodesource')
          end

          it '::nodejs::repo::nodesource::yum should be in the catalog' do
            should contain_class('nodejs::repo::nodesource::yum')
          end

          it 'the nodesource and nodesource-source repos should contain the right description and baseurl' do
            should contain_yumrepo('nodesource').with({
              'baseurl' => repo_baseurl,
              'descr'   => repo_descr,
            })

            should contain_yumrepo('nodesource-source').with({
              'baseurl' => repo_source_baseurl,
              'descr'   => repo_source_descr,
            })
          end
        end

        context 'and repo_enable_src set to true' do
          let :params do
            default_params.merge!({
              :repo_enable_src => true,
            })
          end

          it 'the yumrepo resource nodesource-source should contain enabled = 1' do
            should contain_yumrepo('nodesource-source').with({
              'enabled' => '1',
            })
          end
        end

        context 'and repo_enable_src set to false' do
          let :params do
            default_params.merge!({
              :repo_enable_src => false,
            })
          end

          it 'the yumrepo resource should contain enabled = 0' do
            should contain_yumrepo('nodesource-source').with({
              'enabled' => '0',
            })
          end
        end

        context 'and repo_priority set to 50' do
          let :params do
            default_params.merge!({
              :repo_priority => '50',
            })
          end

          it 'the yumrepo resource nodesource-source should contain priority = 50' do
            should contain_yumrepo('nodesource-source').with({
              'priority' => '50',
            })
          end
        end

        context 'and repo_priority not set' do
          let :params do
            default_params.merge!({
              :repo_priority => 'absent',
            })
          end

          it 'the yumrepo resource nodesource-source should contain priority = absent' do
            should contain_yumrepo('nodesource-source').with({
              'priority' => 'absent',
            })
          end
        end

        context 'and repo_ensure set to present' do
          let :params do
            default_params.merge!({
              :repo_ensure => 'present',
            })
          end

          it 'the nodesource yum repo files should exist' do
            should contain_yumrepo('nodesource')
            should contain_yumrepo('nodesource-source')
          end
        end

        context 'and repo_ensure set to absent' do
          let :params do
            default_params.merge!({
              :repo_ensure => 'absent',
            })
          end

          it 'the nodesource yum repo files should not exist' do
            should contain_yumrepo('nodesource').with({
              'enabled' => 'absent',
            })
            should contain_yumrepo('nodesource-source').with({
              'enabled' => 'absent',
            })
          end
        end

        context 'and repo_proxy set to absent' do
          let :params do
            default_params.merge!({
              :repo_proxy => 'absent',
            })
          end

          it 'the yumrepo resource should contain proxy = absent' do
            should contain_yumrepo('nodesource').with({
              'proxy' => 'absent',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy' => 'absent',
            })
          end
        end

        context 'and repo_proxy set to http://proxy.localdomain.com' do
          let :params do
            default_params.merge!({
              :repo_proxy => 'http://proxy.localdomain.com',
            })
          end

          it 'the yumrepo resource should contain proxy = http://proxy.localdomain.com' do
            should contain_yumrepo('nodesource').with({
              'proxy' => 'http://proxy.localdomain.com',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy' => 'http://proxy.localdomain.com',
            })
          end
        end

        context 'and repo_proxy_password set to absent' do
          let :params do
            default_params.merge!({
              :repo_proxy_password => 'absent',
            })
          end

          it 'the yumrepo resource should contain proxy_password = absent' do
            should contain_yumrepo('nodesource').with({
              'proxy_password' => 'absent',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy_password' => 'absent',
            })
          end
        end

        context 'and repo_proxy_password set to password' do
          let :params do
            default_params.merge!({
              :repo_proxy_password => 'password',
            })
          end

          it 'the yumrepo resource should contain proxy_password = password' do
            should contain_yumrepo('nodesource').with({
              'proxy_password' => 'password',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy_password' => 'password',
            })
          end
        end

        context 'and repo_proxy_username set to absent' do
          let :params do
            default_params.merge!({
              :repo_proxy_username => 'absent',
            })
          end

          it 'the yumrepo resource should contain proxy_username = absent' do
            should contain_yumrepo('nodesource').with({
              'proxy_username' => 'absent',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy_username' => 'absent',
            })
          end
        end

        context 'and repo_proxy_username set to proxyuser' do
          let :params do
            default_params.merge!({
              :repo_proxy_username => 'proxyuser',
            })
          end

          it 'the yumrepo resource should contain proxy_username = proxyuser' do
            should contain_yumrepo('nodesource').with({
              'proxy_username' => 'proxyuser',
            })
            should contain_yumrepo('nodesource-source').with({
              'proxy_username' => 'proxyuser',
            })
          end
        end
      end

      context 'with manage_package_repo set to false' do
        let (:params) {{
          :manage_package_repo => false,
        }}

        it '::nodejs::repo::nodesource should not be in the catalog' do
          should_not contain_class('::nodejs::repo::nodesource')
        end
      end

      # nodejs_debug_package_ensure
      context 'with nodejs_debug_package_ensure set to present' do
        let (:params) { { :nodejs_debug_package_ensure => 'present',} }

        it 'the nodejs package with debugging symbols should be installed' do
          should contain_package('nodejs-debuginfo').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with nodejs_debug_package_ensure set to absent' do
        let (:params) { { :nodejs_debug_package_ensure => 'absent',} }

        it 'the nodejs package with debugging symbols should not be present' do
          should contain_package('nodejs-debuginfo').with({
            'ensure' => 'absent',
          })
        end
      end

      # nodejs_dev_package_ensure
      context 'with nodejs_dev_package_ensure set to present' do
        let (:params) { { :nodejs_dev_package_ensure => 'present',} }

        it 'the nodejs development package should be installed' do
          should contain_package('nodejs-devel').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with nodejs_dev_package_ensure set to absent' do
        let (:params) { { :nodejs_dev_package_ensure => 'absent',} }

        it 'the nodejs development package should not be present' do
          should contain_package('nodejs-devel').with({
            'ensure' => 'absent',
          })
        end
      end

      # nodejs_package_ensure
      context 'with nodejs_package_ensure set to present' do
        let (:params) { { :nodejs_package_ensure => 'present',} }

        it 'the nodejs package should be present' do
          should contain_package('nodejs').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with nodejs_package_ensure set to absent' do
        let (:params) { { :nodejs_package_ensure => 'absent',} }

        it 'the nodejs package should be absent' do
          should contain_package('nodejs').with({
            'ensure' => 'absent',
          })
        end
      end

      # npm_package_ensure
      context 'with npm_package_ensure set to present' do
        let (:params) { { :npm_package_ensure => 'present',} }

        it 'the npm package should be present' do
          should contain_package('npm').with({
            'ensure' => 'present',
          })
        end
      end

      context 'with npm_package_ensure set to absent' do
        let (:params) { { :npm_package_ensure => 'absent',} }

        it 'the npm package should be absent' do
          should contain_package('npm').with({
            'ensure' => 'absent',
          })
        end
      end
    end
  end

  context 'when running on Suse' do
    let :facts do
      {
        :osfamily        => 'Suse',
        :operatingsystem => 'SLES',
      }

    end

    # nodejs_debug_package_ensure
    context 'with nodejs_debug_package_ensure set to present' do
      let (:params) { { :nodejs_debug_package_ensure => 'present',} }

      it 'the nodejs package with debugging symbols should be installed' do
        should contain_package('nodejs-debuginfo').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_debug_package_ensure set to absent' do
      let (:params) { { :nodejs_debug_package_ensure => 'absent',} }

      it 'the nodejs package with debugging symbols should not be present' do
        should contain_package('nodejs-debuginfo').with({
          'ensure' => 'absent',
        })
      end
    end

    # nodejs_dev_package_ensure
    context 'with nodejs_dev_package_ensure set to present' do
      let (:params) { { :nodejs_dev_package_ensure => 'present',} }

      it 'the nodejs development package should be installed' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_dev_package_ensure set to absent' do
      let (:params) { { :nodejs_dev_package_ensure => 'absent',} }

      it 'the nodejs development package should not be present' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'absent',
        })
      end
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('nodejs').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('nodejs').with({
          'ensure' => 'absent',
        })
      end
    end

    # npm_package_ensure
    context 'with npm_package_ensure set to present' do
      let (:params) { { :npm_package_ensure => 'present',} }

      it 'the npm package should be present' do
        should contain_package('npm').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with npm_package_ensure set to absent' do
      let (:params) { { :npm_package_ensure => 'absent',} }

      it 'the npm package should be absent' do
        should contain_package('npm').with({
          'ensure' => 'absent',
        })
      end
    end
  end
  
  context 'when running on Archlinux' do
    let :facts do
      {
        :osfamily        => 'Archlinux',
        :operatingsystem => 'Archlinux',
      }
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('nodejs').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('nodejs').with({
          'ensure' => 'absent',
        })
      end
    end
  end

  context 'when running on FreeBSD' do
    let :facts do
      {
        :osfamily        => 'FreeBSD',
        :operatingsystem => 'FreeBSD',
      }
    end

    # nodejs_dev_package_ensure
    context 'with nodejs_dev_package_ensure set to present' do
      let (:params) { { :nodejs_dev_package_ensure => 'present',} }

      it 'the nodejs development package should be installed' do
        should contain_package('www/node-devel').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_dev_package_ensure set to absent' do
      let (:params) { { :nodejs_dev_package_ensure => 'absent',} }

      it 'the nodejs development package should not be present' do
        should contain_package('www/node-devel').with({
          'ensure' => 'absent',
        })
      end
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('www/node').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('www/node').with({
          'ensure' => 'absent',
        })
      end
    end

    # npm_package_ensure
    context 'with npm_package_ensure set to present' do
      let (:params) { { :npm_package_ensure => 'present',} }

      it 'the npm package should be present' do
        should contain_package('www/npm').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with npm_package_ensure set to absent' do
      let (:params) { { :npm_package_ensure => 'absent',} }

      it 'the npm package should be absent' do
        should contain_package('www/npm').with({
          'ensure' => 'absent',
        })
      end
    end
  end

  context 'when running on OpenBSD' do
    let :facts do
      {
        :osfamily        => 'OpenBSD',
        :operatingsystem => 'OpenBSD',
      }
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('node').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('node').with({
          'ensure' => 'absent',
        })
      end
    end
  end

  context 'when running on Darwin' do
    let :facts do
      {
      :osfamily        => 'Darwin',
      :operatingsystem => 'Darwin',
      }
    end

    # nodejs_dev_package_ensure
    context 'with nodejs_dev_package_ensure set to present' do
      let (:params) { { :nodejs_dev_package_ensure => 'present',} }

      it 'the nodejs development package should be installed' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_dev_package_ensure set to absent' do
      let (:params) { { :nodejs_dev_package_ensure => 'absent',} }

      it 'the nodejs development package should not be present' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'absent',
        })
      end
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('nodejs').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('nodejs').with({
          'ensure' => 'absent',
        })
      end
    end

    # npm_package_ensure
    context 'with npm_package_ensure set to present' do
      let (:params) { { :npm_package_ensure => 'present',} }

      it 'the npm package should be present' do
        should contain_package('npm').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with npm_package_ensure set to absent' do
      let (:params) { { :npm_package_ensure => 'absent',} }
  
      it 'the npm package should be absent' do
        should contain_package('npm').with({
          'ensure' => 'absent',
        })
      end
    end
  end
  
  context 'when running on Windows' do
    let :facts do
      { :osfamily        => 'Windows',
        :operatingsystem => 'Windows',
      }
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('nodejs').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('nodejs').with({
          'ensure' => 'absent',
        })
      end
    end

    # npm_package_ensure
    context 'with npm_package_ensure set to present' do
      let (:params) { { :npm_package_ensure => 'present',} }

      it 'the npm package should be present' do
        should contain_package('npm').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with npm_package_ensure set to absent' do
      let (:params) { { :npm_package_ensure => 'absent',} }

      it 'the npm package should be absent' do
        should contain_package('npm').with({
          'ensure' => 'absent',
        })
      end
    end
  end

  context 'when running on Gentoo' do
    let :facts do
      { :osfamily => 'Linux', :operatingsystem => 'Gentoo',}
    end

    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }

      it 'the nodejs package should be present' do
        should contain_package('net-libs/nodejs').with({
          'ensure' => 'present',
        })
      end
    end

    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }

      it 'the nodejs package should be absent' do
        should contain_package('net-libs/nodejs').with({
          'ensure' => 'absent',
        })
      end
    end

    context 'with use_flags set to npm, snapshot' do
      let (:params) { { :use_flags => [ 'npm', 'snapshot' ],} }

      it 'the nodejs package should have npm, snapshot use flags' do
        should contain_package_use('net-libs/nodejs').with({
          'use' => [ 'npm', 'snapshot'],
        })
      end
    end
  end

  context 'when running on Amazon Linux 2014.09' do
    let :facts do
      { :osfamily               => 'Linux',
        :operatingsystem        => 'Amazon',
        :operatingsystemrelease => '2014.09',
      }
    end

    repo_baseurl        = 'https://rpm.nodesource.com/pub/el/7/$basearch'
    repo_source_baseurl = 'https://rpm.nodesource.com/pub/el/7/SRPMS'
    repo_descr          = 'Node.js Packages for Enterprise Linux 7 - $basearch'
    repo_source_descr   = 'Node.js for Enterprise Linux 7 - $basearch - Source'

    # manage_package_repo
    context 'with manage_package_repo set to true' do
      let (:default_params) { { :manage_package_repo => true,} }

      context 'and repo_class set to ::nodejs::repo::nodesource' do
        let :params do
          default_params.merge!({
            :repo_class => 'nodejs::repo::nodesource',
          })
        end

        it '::nodejs::repo::nodesource should be in the catalog' do
          should contain_class('nodejs::repo::nodesource')
        end

        it '::nodejs::repo::nodesource::yum should be in the catalog' do
          should contain_class('nodejs::repo::nodesource::yum')
        end

        it 'the nodesource and nodesource-source repos should contain the right description and baseurl' do
          should contain_yumrepo('nodesource').with({
            'baseurl' => repo_baseurl,
            'descr'   => repo_descr,
          })

          should contain_yumrepo('nodesource-source').with({
            'baseurl' => repo_source_baseurl,
            'descr'   => repo_source_descr,
          })
        end
      end

      context 'and repo_enable_src set to true' do
        let :params do
          default_params.merge!({
            :repo_enable_src => true,
          })
        end

        it 'the yumrepo resource nodesource-source should contain enabled = 1' do
          should contain_yumrepo('nodesource-source').with({
            'enabled' => '1',
          })
        end
      end

      context 'and repo_enable_src set to false' do
        let :params do
          default_params.merge!({
            :repo_enable_src => false,
          })
        end

        it 'the yumrepo resource should contain enabled = 0' do
          should contain_yumrepo('nodesource-source').with({
            'enabled' => '0',
          })
        end
      end

      context 'and repo_ensure set to present' do
        let :params do
          default_params.merge!({
            :repo_ensure => 'present',
          })
        end

        it 'the nodesource yum repo files should exist' do
          should contain_yumrepo('nodesource')
          should contain_yumrepo('nodesource-source')
        end
      end

      context 'and repo_ensure set to absent' do
        let :params do
          default_params.merge!({
            :repo_ensure => 'absent',
          })
        end

        it 'the nodesource yum repo files should not exist' do
          should contain_yumrepo('nodesource').with({
            'enabled' => 'absent',
          })
          should contain_yumrepo('nodesource-source').with({
            'enabled' => 'absent',
          })
        end
      end

      context 'and repo_proxy set to absent' do
        let :params do
          default_params.merge!({
            :repo_proxy => 'absent',
          })
        end

        it 'the yumrepo resource should contain proxy = absent' do
          should contain_yumrepo('nodesource').with({
            'proxy' => 'absent',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy' => 'absent',
          })
        end
      end

      context 'and repo_proxy set to http://proxy.localdomain.com' do
        let :params do
          default_params.merge!({
            :repo_proxy => 'http://proxy.localdomain.com',
          })
        end

        it 'the yumrepo resource should contain proxy = http://proxy.localdomain.com' do
          should contain_yumrepo('nodesource').with({
            'proxy' => 'http://proxy.localdomain.com',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy' => 'http://proxy.localdomain.com',
          })
        end
      end

      context 'and repo_proxy_password set to absent' do
        let :params do
          default_params.merge!({
            :repo_proxy_password => 'absent',
          })
        end

        it 'the yumrepo resource should contain proxy_password = absent' do
          should contain_yumrepo('nodesource').with({
            'proxy_password' => 'absent',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy_password' => 'absent',
          })
        end
      end

      context 'and repo_proxy_password set to password' do
        let :params do
          default_params.merge!({
            :repo_proxy_password => 'password',
          })
        end

        it 'the yumrepo resource should contain proxy_password = password' do
          should contain_yumrepo('nodesource').with({
            'proxy_password' => 'password',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy_password' => 'password',
          })
        end
      end

      context 'and repo_proxy_username set to absent' do
        let :params do
          default_params.merge!({
            :repo_proxy_username => 'absent',
          })
        end

        it 'the yumrepo resource should contain proxy_username = absent' do
          should contain_yumrepo('nodesource').with({
            'proxy_username' => 'absent',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy_username' => 'absent',
          })
        end
      end

      context 'and repo_proxy_username set to proxyuser' do
        let :params do
          default_params.merge!({
            :repo_proxy_username => 'proxyuser',
          })
        end

        it 'the yumrepo resource should contain proxy_username = proxyuser' do
          should contain_yumrepo('nodesource').with({
            'proxy_username' => 'proxyuser',
          })
          should contain_yumrepo('nodesource-source').with({
            'proxy_username' => 'proxyuser',
          })
        end
      end
    end

    context 'with manage_package_repo set to false' do
      let (:params) {{
        :manage_package_repo => false,
      }}

      it '::nodejs::repo::nodesource should not be in the catalog' do
        should_not contain_class('::nodejs::repo::nodesource')
      end
    end

    # nodejs_debug_package_ensure
    context 'with nodejs_debug_package_ensure set to present' do
      let (:params) { { :nodejs_debug_package_ensure => 'present',} }
  
      it 'the nodejs package with debugging symbols should be installed' do
        should contain_package('nodejs-debuginfo').with({
          'ensure' => 'present',
        })
      end
    end
  
    context 'with nodejs_debug_package_ensure set to absent' do
      let (:params) { { :nodejs_debug_package_ensure => 'absent',} }
  
      it 'the nodejs package with debugging symbols should not be present' do
        should contain_package('nodejs-debuginfo').with({
          'ensure' => 'absent',
        })
      end
    end
  
    # nodejs_dev_package_ensure
    context 'with nodejs_dev_package_ensure set to present' do
      let (:params) { { :nodejs_dev_package_ensure => 'present',} }
  
      it 'the nodejs development package should be installed' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'present',
        })
      end
    end
  
    context 'with nodejs_dev_package_ensure set to absent' do
      let (:params) { { :nodejs_dev_package_ensure => 'absent',} }
  
      it 'the nodejs development package should not be present' do
        should contain_package('nodejs-devel').with({
          'ensure' => 'absent',
        })
      end
    end
  
    # nodejs_package_ensure
    context 'with nodejs_package_ensure set to present' do
      let (:params) { { :nodejs_package_ensure => 'present',} }
  
      it 'the nodejs package should be present' do
        should contain_package('nodejs').with({
          'ensure' => 'present',
        })
      end
    end
  
    context 'with nodejs_package_ensure set to absent' do
      let (:params) { { :nodejs_package_ensure => 'absent',} }
  
      it 'the nodejs package should be absent' do
        should contain_package('nodejs').with({
          'ensure' => 'absent',
        })
      end
    end
  
    # npm_package_ensure
    context 'with npm_package_ensure set to present' do
      let (:params) { { :npm_package_ensure => 'present',} }
  
      it 'the npm package should be present' do
        should contain_package('npm').with({
          'ensure' => 'present',
        })
      end
    end
  
    context 'with npm_package_ensure set to absent' do
      let (:params) { { :npm_package_ensure => 'absent',} }
  
      it 'the npm package should be absent' do
        should contain_package('npm').with({
          'ensure' => 'absent',
        })
      end
    end
  end
end
