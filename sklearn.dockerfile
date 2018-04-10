FROM jeff1evesque/ml-base:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY hiera $ROOT_PROJECT/hiera
COPY puppet/environment/$ENVIRONMENT/modules/sklearn $ROOT_PUPPET/code/modules/sklearn

## provision with puppet
RUN $PUPPET apply -e 'class { sklearn: }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
