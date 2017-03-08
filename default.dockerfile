FROM ubuntu:14.04

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## copy files into container
RUN mkdir /var/machine-learning
COPY . /var/machine-learning

## install git, wget, pip
##
##  Note: r10k requires 'git' installed
##
RUN apt-get -y update
RUN apt-get -y install git=1:1.9.1-1ubuntu0.3
RUN apt-get -y install wget=1.15-1ubuntu1.14.04.2
RUN apt-get -y install python-pip=1.5.4-1ubuntu4

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb
RUN dpkg -i puppetlabs-release-pc1-trusty.deb
RUN apt-get -y update
RUN apt-get -y install puppet-agent

## install r10k
RUN apt-get -y install rubygems-integration=1.5
RUN gem install r10k -v 2.5.2

## install pytest-cov
RUN pip install pytest-cov==2.4.0

## install puppet modules using puppetfile with r10k
RUN mkdir -p $ENVIRONMENT_DIR/modules_contrib/
RUN PUPPETFILE=$ENVIRONMENT_DIR/Puppetfile PUPPETFILE_DIR=$ENVIRONMENT_DIR/modules_contrib/ r10k puppetfile install

## remove npm: it will be installed via puppet
RUN npm -v
RUN node -v
RUN nodejs -v

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/package/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/sklearn/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/system/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/compiler/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test --debug
