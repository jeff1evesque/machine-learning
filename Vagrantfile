# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  ## Variables (ruby syntax)
 required_plugins  = %w(vagrant-r10k vagrant-vbguest vagrant-triggers vagrant-puppet-install)
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

  ## ensure puppet modules directory on the host before 'vagrant up'
  config.trigger.before :up do
    run 'mkdir -p puppet/environment/development/modules'
    run 'mkdir -p puppet/environment/development/modules_contrib'
  end

  ## Every Vagrant development environment requires a box. You can search for
  #  boxes at https://atlas.hashicorp.com/search.
  config.vm.box = 'ubuntu/trusty64'

  ## Ensure puppet installed within guest
  config.puppet_install.puppet_version = '4.3.2'

  ## Create a forwarded port mapping which allows access to a specific port
  #  within the machine from a port on the host machine. In the example below,
  #  accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network 'forwarded_port', guest: 5000, host: 8080
  config.vm.network 'forwarded_port', guest: 443, host: 8585

  ## Run r10k
  config.r10k.puppet_dir      = 'puppet/environment/development'
  config.r10k.puppetfile_path = 'puppet/environment/development/Puppetfile'

  ## Custom Manifest: install needed packages
  #
  #  Note: future parser allow array iteration in the puppet manifest
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'install_packages.pp'
  end

  ## Custom Manifest: build scikit-learn
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'install_sklearn.pp'
  end

  ## Custom Manifest: ensure vagrant-mounted event
  #
  #  Note: future parser allow heredoc syntax in the puppet manifest (since puppet 3.5)
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'vagrant_mounted.pp'
  end

  ## Custom Manifest: install redis client / server
  #
  #  Note: future parser allow heredoc syntax in the puppet manifest (since puppet 3.5)
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'configure_redis.pp'
  end

  ## Custom Manifest: configure system (i.e. system timezone)
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'configure_system.pp'
  end

  ## Custom Manifest: define webcompilers
  #
  #  Note: future parser allow heredoc sytnax (since puppet 3.5), and allows array
  #        iteration in the puppet manifest.
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'compile_asset.pp'
  end

  ## Custom Manifest: install, and configure SQL database
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'setup_database.pp'
  end

  ## Custom Manifest: start webserver
  #
  #  Note: future parser allow heredoc syntax in the puppet manifest (since puppet 3.5)
  config.vm.provision 'puppet' do |puppet|
    puppet.environment_path = 'puppet/environment'
    puppet.environment      = 'development'
    puppet.manifests_path   = 'puppet/environment/development/manifests'
    puppet.module_path      = ['puppet/environment/development/modules_contrib', 'puppet/environment/development/modules']
    puppet.manifest_file    = 'start_webserver.pp'
  end

  # clean up files on the host after 'vagrant destroy'
  config.trigger.after :destroy do
    run 'rm -Rf log'
    run 'rm -Rf build'
    run 'rm -Rf interface/static/css'
    run 'rm -Rf interface/static/img'
    run 'rm -Rf interface/static/js'
    run 'rm -Rf puppet/environment/development/modules_contrib'
    run 'rm -f src/js/.gitignore'
    run 'rm -f src/js/support_vector.js'
  end
  
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end