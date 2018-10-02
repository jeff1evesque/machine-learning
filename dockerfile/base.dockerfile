FROM ubuntu:16.04

## environment variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ENV ENVPATH $ROOT_PUPPET/code/environment/$ENVIRONMENT
ENV PUPPET_VERSION puppet5-release-xenial.deb

## ensure directory
RUN mkdir -p $ROOT_PROJECT/log $ROOT_PUPPET/code/environment/$ENVIRONMENT $ROOT_PUPPET/puppet/hiera $ROOT_PUPPET/code/modules_contrib

##
## install git, wget, puppet
##
##  Note: r10k requires 'git' installed
##
RUN apt-get -y update
RUN apt-get -y install wget=1.17.1-1ubuntu*
RUN wget https://apt.puppetlabs.com/$PUPPET_VERSION
RUN dpkg -i $PUPPET_VERSION
RUN apt-get -y update
RUN apt-get -y install git=1:2.7.4-0ubuntu* puppet-agent=5.5*

## copy configs
COPY puppet/environment/$ENVIRONMENT/Puppetfile $ENVPATH
COPY puppet/environment/$ENVIRONMENT/modules $ROOT_PUPPET/code/modules
COPY hiera $ROOT_PUPPET/puppet/hiera
COPY hiera.yaml $ROOT_PUPPET/puppet

## install ruby
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN cd /tmp && \curl -sSL https://get.rvm.io -o rvm.sh
RUN cat /tmp/rvm.sh | bash -s stable
RUN source /usr/local/rvm/scripts/rvm
RUN rvm list known && rvm install 2.5.1

## install r10k
##
## Note: r10k requires 'semantic_puppet' at '0.1.0':
##
##       https://github.com/jeff1evesque/machine-learning/issues/2991
##
RUN apt-get -y install rubygems-integration=1.10
RUN gem install semantic_puppet:0.1.0 puppet_forge:2.2.9 r10k:3.0.2

## install puppet modules using puppetfile with r10k
RUN PUPPETFILE=$ENVPATH/Puppetfile PUPPETFILE_DIR=$CONTRIB_MODULES r10k puppetfile install

## provision with puppet
RUN $PUPPET apply apply -e 'class { system: }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
