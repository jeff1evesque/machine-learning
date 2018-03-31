FROM ubuntu:14.04

## environment variables
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV ENVIRONMENT docker

## ensure directory
RUN mkdir -p /var/machine-learning/log
RUN mkdir -p $ROOT_PUPPET/code/environment/$ENVIRONMENT
RUN mkdir -p $ROOT_PUPPET/puppet/hiera
RUN mkdir -p $ROOT_PUPPET/code/modules_contrib

## environment variables
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ENV ENVPATH $ROOT_PUPPET/code/environment/$ENVIRONMENT

## install git, wget, pip
##
##  Note: r10k requires 'git' installed
##
RUN apt-get -y update
RUN apt-get -y install git=1:1.9.1-1ubuntu0.7
RUN apt-get -y install wget=1.15-1ubuntu1.14.04*
RUN apt-get -y install python-pip=1.5.4-1ubuntu4

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb
RUN dpkg -i puppetlabs-release-pc1-trusty.deb
RUN apt-get -y update
RUN apt-get -y install puppet-agent

## copy puppet
COPY puppet/environment/$ENVIRONMENT/Puppetfile $ENVPATH
COPY puppet/environment/$ENVIRONMENT/modules $ROOT_PUPPET/code/modules
COPY hiera $ROOT_PUPPET/puppet/hiera
COPY hiera.yaml $ROOT_PUPPET/puppet

## install r10k
##
## Note: r10k requires 'semantic_puppet' at '0.1.0':
##
##       https://github.com/jeff1evesque/machine-learning/issues/2991
##
RUN apt-get -y install rubygems-integration=1.5
RUN gem install semantic_puppet -v 0.1.0
RUN gem install puppet_forge -v 2.2.5
RUN gem install r10k -v 2.5.5

## install puppet modules using puppetfile with r10k
RUN PUPPETFILE=$ENVPATH/Puppetfile PUPPETFILE_DIR=$CONTRIB_MODULES r10k puppetfile install

## provision with puppet
RUN $PUPPET apply $MODULES/package/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
RUN $PUPPET apply $MODULES/system/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
