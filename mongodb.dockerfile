FROM jeff1evesque/ml-base:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## provision container
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN apt-get install -y --no-install-recommends software-properties-common
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update && apt-get install -y mongodb-org
RUN mkdir -p /data/db

## copy files into container
COPY puppet/environment/$ENVIRONMENT/modules/mongodb $ROOT_PUPPET/code/modules/mongodb

## configuration file
RUN $PUPPET apply -e 'class { mongodb: \
    run => true, \
    security_authorization => false \
}' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
ENTRYPOINT ["/usr/bin/mongod"]
CMD ["-f", "/etc/mongod.conf"]