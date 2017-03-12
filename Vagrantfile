## -*- mode: ruby -*-
## vi: set ft=ruby :

## require ruby modules
require 'yaml'

## mongodb: get server hostnames
current_dir    = File.join(File.expand_path(__FILE__))
db_config      = YAML.load_file(Pathname(current_dir).join(
    'hiera',
    'database.yaml'
))
mongodb_nodes = db_config['database']['mongodb_cluster']['hostname']

## mongodb: array of configuration files
mongodb_config = Array.new
mongodb_nodes.map { |server|
    YAML.load_file("#{current_dir}/hiera/nodes/#{server}.mongodb.com.yaml")
}

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

    ## configure mongodb cluster
    mongodb_servers.each do |server|
        config.vm.define server['database']['mongodb_cluster']['node']['hostname'] do |srv|
            ## local variables
            puppet_environment  = 'mongodb'
            node                = srv['database']['mongodb_cluster']['node']
            fqdn                = node['fqdn']
            host_ip             = node['ip']
            hostname            = node['hostname']
            memory              = node['memory']
            atlas_repo          = node['atlas_repo']
            atlas_box           = node['atlas_box']
            atlas_checksum      = node['atlas_checksum']
            atlas_checksum_type = node['atlas_checksum_type']
            puppet_version      = node['puppet_version']

            ## custom box settings
            srv.vm.box                        = "#{atlas_repo}/#{atlas_box}"
            srv.vm.box_download_checksum      = atlas_checksum
            srv.vm.box_url                    = "https://atlas.hashicorp.com/#{atlas_repo}/boxes/#{atlas_box}/versions/#{box_version}/providers/virtualbox.box"
            srv.vm.box_download_checksum_type = atlas_checksum_type

            ## increase RAM
            srv.vm.provider 'virtualbox' do |v|
                v.customize ['modifyvm', :id, '--memory', memory]
            end

            ## ensure puppet directories
            srv.trigger.before :up do
                run "mkdir -p puppet/environment/#{puppet_environment}/modules"
                run "mkdir -p puppet/environment/#{puppet_environment}/modules_contrib"
            end

            ## Ensure puppet installed within guest
            srv.puppet_install.puppet_version = puppet_version

            ## ensure puppet modules directory on the host before 'vagrant up'
            srv.trigger.before :up do
                run "mkdir -p puppet/environment/#{puppet_environment}/modules_contrib"
            end

            ## Run r10k
            srv.r10k.puppet_dir      = "puppet/environment/#{puppet_environment}"
            srv.r10k.puppetfile_path = "puppet/environment/#{puppet_environment}/Puppetfile"

            ## provision host: needed by puppet
            srv.vm.provision 'shell', inline: <<-SHELL
                cd current_dir/utility/
                ./configure-host fqdn host_ip hostname
                ./configure-puppet fqdn host_ip environment
            SHELL

            ## provision mongodb
            srv.vm.provision 'puppet' do |puppet|
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
            srv.trigger.after :destroy do
                run "rm -Rf puppet/environment/#{puppet_environment}/modules_contrib"
            end
        end
    end

    ## general application
    config.vm.define 'main' do |main|
        ## local variables
        atlas_repo          = 'jeff1evesque'
        atlas_box           = 'trusty64'
        box_version         = '1.0.0'
        puppet_environment  = 'vagrant'

        ## increase RAM to ensure scrypt doesn't exhaust memory
        main.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--memory', '6000']
        end

        ## ensure puppet modules directory on the host before 'vagrant up'
        main.trigger.before :up do
            run "mkdir -p puppet/environment/#{puppet_environment}/modules_contrib"
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
            run 'rm -Rf src/jsx/node_modules'
            run 'rm -f src/js/.gitignore'
            run 'rm -f src/js/content.js'
            run 'find . -name "*.pyc" -type f -exec rm -r {} +'
            run 'find . -name __pycache__ -type d -exec rm -r {} +'
            run 'find . -name .cache -type d -exec rm -r {} +'
        end
    end
end