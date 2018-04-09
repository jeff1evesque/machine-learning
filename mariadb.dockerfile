FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY puppet/environment/$ENVIRONMENT/modules/mariadb $ROOT_PUPPET/code/modules/mariadb

## provision with puppet
RUN $PUPPET apply -e 'class { mariadb: run => false }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## create database (non-idempotent)
RUN cd $ROOT_PUPPET/code/modules/mariadb/scripts && python setup_tables.py $ROOT_PUPPET/puppet",

## executed everytime container starts
CMD ["/bin/sh", "-c", "mysqld"]