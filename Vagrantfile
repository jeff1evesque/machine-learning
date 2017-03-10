## -*- mode: ruby -*-
## vi: set ft=ruby :

## All Vagrant configuration is done below. The "2" in Vagrant.configure
## configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
## you're doing.
Vagrant.configure(2) do |config|
    ## Variables (ruby syntax)
    atlas_repo       = 'jeff1evesque'
    atlas_box        = 'trusty64'
    box_version      = '1.0.0'

    required_plugins = %w(vagrant-r10k vagrant-triggers vagrant-puppet-install)
    plugin_installed = false

    ## Install Vagrant Plugins
    required_plugins.each do |plugin|
        unless Vagrant.has_plugin? plugin
            system "vagrant plugin install #{plugin}"
            plugin_installed = true
        end
    end

    ## Restart Vagrant: if new plugin installed
    if plugin_installed == true
        exec "vagrant #{ARGV.join(' ')}"
    end

    ## mongodb cluster
    config.vm.define 'aristotle' do |aristotle|
        environment = 'mongodb_cluster'

        aristotle.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '1000']
        end

        aristotle.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules"
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        aristotle.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        aristotle.vm.box_download_checksum      = 'c26da6ba1c169bdc6e9168125ddb0525'
        aristotle.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
        aristotle.vm.box_download_checksum_type = 'md5'

        ## Ensure puppet installed within guest
        aristotle.puppet_install.puppet_version = '4.9.3'

        ## ensure puppet modules directory on the host before 'vagrant up'
        aristotle.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        ## Run r10k
        aristotle.r10k.puppet_dir      = "puppet/environment/#{environment}"
        aristotle.r10k.puppetfile_path = "puppet/environment/#{environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        aristotle.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = environment
            puppet.manifests_path    = "puppet/environment/#{environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{environment}/modules_contrib",
                "puppet/environment/#{environment}/modules",
            ]
            puppet.manifest_file     = 'site.pp'
            puppet.hiera_config_path = 'hiera.yaml'
        end

        ## clean up files on the host after 'vagrant destroy'
        aristotle.trigger.after :destroy do
            run 'rm -Rf puppet/environment/*/modules_contrib'
        end
    end

    ## mongodb cluster
    config.vm.define 'socrates' do |socrates|
        environment = 'mongodb_cluster'

        ## increase RAM
        socrates.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '1000']
        end

        socrates.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules"
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        socrates.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        socrates.vm.box_download_checksum      = 'c26da6ba1c169bdc6e9168125ddb0525'
        socrates.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
        socrates.vm.box_download_checksum_type = 'md5'

        ## Ensure puppet installed within guest
        socrates.puppet_install.puppet_version = '4.9.3'

        ## ensure puppet modules directory on the host before 'vagrant up'
        socrates.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        ## Run r10k
        socrates.r10k.puppet_dir      = "puppet/environment/#{environment}"
        socrates.r10k.puppetfile_path = "puppet/environment/#{environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        socrates.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = environment
            puppet.manifests_path    = "puppet/environment/#{environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{environment}/modules_contrib",
                "puppet/environment/#{environment}/modules",
            ]
            puppet.manifest_file     = 'site.pp'
            puppet.hiera_config_path = 'hiera.yaml'
        end

        ## clean up files on the host after 'vagrant destroy'
        socrates.trigger.after :destroy do
            run 'rm -Rf puppet/environment/*/modules_contrib'
        end
    end

    ## mongodb cluster
    config.vm.define 'plato' do |socrates|
        environment = 'mongodb_cluster'

        ## increase RAM
        plato.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '1000']
        end

        plato.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules"
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        plato.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        plato.vm.box_download_checksum      = 'c26da6ba1c169bdc6e9168125ddb0525'
        plato.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
        plato.vm.box_download_checksum_type = 'md5'

        ## Ensure puppet installed within guest
        plato.puppet_install.puppet_version = '4.9.3'

        ## ensure puppet modules directory on the host before 'vagrant up'
        plato.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        ## Run r10k
        plato.r10k.puppet_dir      = "puppet/environment/#{environment}"
        plato.r10k.puppetfile_path = "puppet/environment/#{environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        plato.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = environment
            puppet.manifests_path    = "puppet/environment/#{environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{environment}/modules_contrib",
                "puppet/environment/#{environment}/modules",
            ]
            puppet.manifest_file     = 'site.pp'
            puppet.hiera_config_path = 'hiera.yaml'
        end

        ## clean up files on the host after 'vagrant destroy'
        plato.trigger.after :destroy do
            run 'rm -Rf puppet/environment/*/modules_contrib'
        end
    end

    ## mongodb cluster
    config.vm.define 'confucious' do |confucious|
        environment = 'mongodb_cluster'

        ## increase RAM
        confucious.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '1000']
        end

        ## ensure puppet modules directory on the host before 'vagrant up'
        confucious.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        confucious.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        confucious.vm.box_download_checksum      = 'c26da6ba1c169bdc6e9168125ddb0525'
        confucious.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
        confucious.vm.box_download_checksum_type = 'md5'

        ## Ensure puppet installed within guest
        confucious.puppet_install.puppet_version = '4.9.3'

        ## Run r10k
        confucious.r10k.puppet_dir      = "puppet/environment/#{environment}"
        confucious.r10k.puppetfile_path = "puppet/environment/#{environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        confucious.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = environment
            puppet.manifests_path    = "puppet/environment/#{environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{environment}/modules_contrib",
                "puppet/environment/#{environment}/modules",
            ]
            puppet.manifest_file     = 'site.pp'
            puppet.hiera_config_path = 'hiera.yaml'
        end

        ## clean up files on the host after 'vagrant destroy'
        confucious.trigger.after :destroy do
            run 'rm -Rf puppet/environment/*/modules_contrib'
        end
    end

    ## general application
    config.vm.define 'main' do |main|
        environment = 'vagrant'

        ## increase RAM to ensure scrypt doesn't exhaust memory
        main.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '6000']
        end

        ## ensure puppet modules directory on the host before 'vagrant up'
        main.trigger.before :up do
            run "mkdir -p puppet/environment/#{environment}/modules_contrib"
        end

        main.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        main.vm.box_download_checksum      = 'c26da6ba1c169bdc6e9168125ddb0525'
        main.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
        main.vm.box_download_checksum_type = 'md5'

        ## Ensure puppet installed within guest
        main.puppet_install.puppet_version = '4.9.3'

        ## Create a forwarded port mapping which allows access to a specific port
        ## within the machine from a port on the host machine. In the example below,
        ## accessing "localhost:8080" will access port 80 on the guest machine.
        main.vm.network 'forwarded_port', guest: 5000, host: 8080
        main.vm.network 'forwarded_port', guest: 443, host: 8585

        ## Run r10k
        main.r10k.puppet_dir      = "puppet/environment/#{environment}"
        main.r10k.puppetfile_path = "puppet/environment/#{environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        main.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = environment
            puppet.manifests_path    = "puppet/environment/#{environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{environment}/modules_contrib",
                "puppet/environment/#{environment}/modules",
            ]
            puppet.manifest_file     = 'site.pp'
            puppet.hiera_config_path = 'hiera.yaml'
        end

        ## clean up files on the host after 'vagrant destroy'
        main.trigger.after :destroy do
            run 'rm -Rf log/database'
            run 'rm -Rf log/application'
            run 'rm -Rf log/webcompiler'
            run 'rm -Rf log/webserver'
            run 'rm -Rf build'
            run 'rm -Rf interface/static/css'
            run 'rm -Rf interface/static/img'
            run 'rm -Rf interface/static/js'
            run 'rm -Rf puppet/environment/*/modules_contrib'
            run 'rm -Rf src/jsx/node_modules'
            run 'rm -f src/js/.gitignore'
            run 'rm -f src/js/content.js'
            run 'find . -name "*.pyc" -type f -exec rm -r {} +'
            run 'find . -name __pycache__ -type d -exec rm -r {} +'
            run 'find . -name .cache -type d -exec rm -r {} +'
        end
    end
end