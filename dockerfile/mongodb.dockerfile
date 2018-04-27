FROM jeff1evesque/ml-base:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY hiera $ROOT_PUPPET/puppet/hiera
COPY puppet/environment/$ENVIRONMENT/modules/mongodb $ROOT_PUPPET/code/modules/mongodb

## configuration file
RUN $PUPPET apply -e 'class { mongodb: \
    run                    => true, \
    bindIp                 => "0.0.0.0", \
    security_authorization => false \
}' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/

## define entrypoint script
RUN printf '#!/bin/bash\n\n\
/usr/bin/mongod --fork --config /etc/mongod.conf\n\
cd /root/build && ./create-mongodb-users\n\
sed -i "/#[[:space:]]*security:/s/^#//g" /etc/mongod.conf\n\
sed -i "/#[[:space:]]*authorization:[[:space:]]*enabled/s/^#//g" /etc/mongod.conf\n\
/usr/bin/mongod --shutdown\n\
/usr/bin/mongod --config /etc/mongod.conf\n\
' > entrypoint
RUN chmod 710 entrypoint

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "./entrypoint"]
