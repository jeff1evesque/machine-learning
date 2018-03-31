FROM ml-base

## local variables
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## provision with puppet
RUN $PUPPET apply $MODULES/mariadb/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
CMD ["/bin/sh", "-c", "mysqld"]