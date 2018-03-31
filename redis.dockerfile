FROM ml-base

## local variables
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY puppet/environment/$ENVIRONMENT/modules/redis $ROOT_PUPPET/code/modules/redis

## provision with puppet
RUN $PUPPET apply $MODULES/redis/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
CMD ["/bin/sh", "-c", "redis-server"]
