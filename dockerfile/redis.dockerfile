FROM jeff1evesque/ml-base:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY hiera $ROOT_PUPPET/puppet/hiera
COPY puppet/environment/$ENVIRONMENT/modules/redis $ROOT_PUPPET/code/modules/redis

## provision with puppet
RUN $PUPPET apply -e 'class { redis: run => false }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "redis-server"]
