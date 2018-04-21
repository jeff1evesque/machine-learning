FROM jeff1evesque/ml-base:0.7

## local variables
ENV ENVIRONMENT=docker\
    PUPPET=/opt/puppetlabs/bin/puppet\
    ROOT_PUPPET=/etc/puppetlabs\
    MODULES=$ROOT_PUPPET/code/modules\
    CONTRIB_MODULES=$ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY puppet/environment/$ENVIRONMENT/modules/mariadb $MODULES/mariadb
COPY hiera $ROOT_PUPPET/puppet/hiera

## provision with puppet
RUN $PUPPET apply -e 'class {\
    mariadb:\
}' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## define entrypoint script
RUN printf "#!/bin/bash\n\n\
service mysql start\n\
cd $MODULES/mariadb/scripts\n\
python setup_tables.py $ROOT_PUPPET/puppet\n\
" > entrypoint
RUN chmod 710 entrypoint

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "mysqld"]
