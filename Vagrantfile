## -*- mode: ruby -*-
## vi: set ft=ruby :

## build vagrant instances
Vagrant.configure(2) do |config|
    ## globally configure plugins
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

    ## general application
    config.vm.define 'main' do |main|
        ## local variables
        atlas_repo          = 'jeff1evesque'
        atlas_box           = 'trusty64'
        box_version         = '1.2.0'
        box_checksum        = '0bf7b36547e38adf0424735c9c638e17'
        box_checksum_type   = 'md5'
        puppet_environment  = 'vagrant'

        ## increase RAM to ensure scrypt doesn't exhaust memory
        main.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '1024']
        end

        ## ensure puppet modules directory on the host before 'vagrant up'
        main.trigger.before :up do
            run "mkdir -p puppet/environment/#{puppet_environment}/modules_contrib"
        end

        main.vm.box                        = "#{atlas_repo}/#{atlas_box}"
        main.vm.box_version                = box_version
        main.vm.box_download_checksum      = box_checksum
        main.vm.box_download_checksum_type = box_checksum_type

        ## Ensure puppet installed within guest
        main.puppet_install.puppet_version = '4.9.3'

        ## Create a forwarded port mapping which allows access to a specific port
        ## within the machine from a port on the host machine. In the example below,
        ## accessing "localhost:8080" will access port 80 on the guest machine.
        main.vm.network 'forwarded_port', guest: 5000, host: 8080
        main.vm.network 'forwarded_port', guest: 6000, host: 9090

        ## Run r10k
        main.r10k.puppet_dir      = "puppet/environment/#{puppet_environment}"
        main.r10k.puppetfile_path = "puppet/environment/#{puppet_environment}/Puppetfile"

        ## Custom Manifest: install needed packages
        main.vm.provision 'puppet' do |puppet|
            puppet.environment_path  = 'puppet/environment'
            puppet.environment       = puppet_environment
            puppet.manifests_path    = "puppet/environment/#{puppet_environment}/manifests"
            puppet.module_path       = [
                "puppet/environment/#{puppet_environment}/modules_contrib",
                "puppet/environment/#{puppet_environment}/modules",
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
            run "rm -Rf puppet/environment/#{puppet_environment}/modules_contrib"
            run 'rm -Rf src/node_modules'
            run 'rm -f src/js/.gitignore'
            run 'rm -f src/js/content.js'
            run 'find . -name "*.pyc" -type f -exec rm -r {} +'
            run 'find . -name __pycache__ -type d -exec rm -r {} +'
            run 'find . -name .cache -type d -exec rm -r {} +'
        end
    end
end