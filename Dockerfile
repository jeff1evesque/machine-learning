FROM ubuntu:14.04

## copy files into container
RUN mkdir /var/machine-learning
COPY . /var/machine-learning

## install upstart, git, and wget
#
#  Note: r10k requires 'git' installed
RUN apt-get -y update
RUN apt-get -y install git=1:1.9.1-1ubuntu0.3
RUN apt-get -y install wget=1.15-1ubuntu1.14.04.2

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb
RUN dpkg -i puppetlabs-release-pc1-trusty.deb
RUN apt-get -y update
RUN apt-get -y install puppet-agent

## install r10k
RUN apt-get -y install rubygems-integration=1.5
RUN gem install r10k -v 2.2.0

## install puppet modules using puppetfile with r10k
RUN mkdir -p /var/machine-learning/puppet/environment/development/modules_contrib/
RUN PUPPETFILE=/var/machine-learning/test/Puppetfile PUPPETFILE_DIR=/var/machine-learning/puppet/environment/development/modules_contrib/ r10k puppetfile install

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/install_packages.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/install_sklearn.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/configure_redis.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/configure_system.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/compile_asset.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/setup_database.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/start_webserver.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test

## debug
RUN ls -l /etc/init
RUN cat /etc/init/sass.conf
RUN ls -l /var/machine-learning/puppet/environment/development/modules/compiler/scripts
RUN ls -l /var/machine-learning/interface/static/css
RUN ls -l /var/machine-learning/interface/static/img
RUN ls -l /var/machine-learning/interface/static/js
