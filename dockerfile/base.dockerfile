FROM ubuntu:16.04

## environment variables
ENV ENVIRONMENT=docker\
    PUPPET=/opt/puppetlabs/bin/puppet\
    ROOT_PROJECT=/var/machine-learning\
    ROOT_PUPPET=/etc/puppetlabs\
    MODULES=$ROOT_PUPPET/code/modules\
    CONTRIB_MODULES=$ROOT_PUPPET/code/modules_contrib\
    ENVPATH=$ROOT_PUPPET/code/environment/$ENVIRONMENT\
    PUPPET_VERSION=puppet5-release-xenial.deb

## ensure directory
RUN mkdir -p $ROOT_PROJECT/log $ROOT_PUPPET/code/environment/$ENVIRONMENT $ROOT_PUPPET/puppet/hiera $ROOT_PUPPET/code/modules_contrib

##
## install git, wget, puppet
##
##  Note: r10k requires 'git' installed
##
RUN apt-get -y update
RUN apt-get -y install wget=1.17* curl=7.47*
RUN wget https://apt.puppetlabs.com/$PUPPET_VERSION
RUN dpkg -i $PUPPET_VERSION
RUN apt-get -y update
RUN apt-get -y install git=1:2.7.4-0ubuntu* puppet-agent=5.5*

## copy configs
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
RUN apt-get -y install ruby=1:2.3* rubygems-integration=1.10
RUN gem install semantic_puppet:0.1.0 puppet_forge:2.2.9 r10k:3.0.2

## install puppet modules using puppetfile with r10k
RUN r10k puppetfile install --puppetfile $ENVPATH/Puppetfile --moduledir $CONTRIB_MODULES

## provision with puppet
RUN $PUPPET apply apply -e 'class { system: }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
