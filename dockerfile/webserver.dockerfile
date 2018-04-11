FROM jeff1evesque/ml-sklearn:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## ensure directory
RUN mkdir -p $ROOT_PROJECT/interface $ROOT_PUPPET/brain $ROOT_PUPPET/test

## copy files into container
COPY log interface hiera brain test app.py factory.py __init__.py $ROOT_PROJECT/
COPY puppet/environment/$ENVIRONMENT/modules/webserver $ROOT_PUPPET/code/modules/webserver

##
## provision with puppet: either build a web, or api webserver image.
##
##     docker build -f webserver.dockerfile -t jeff1evesque/ml-webserver:0.7 .
##
##     docker run --hostname webserver-api --name webserver -d jeff1evesque/ml-webserver:0.7 '0.0.0.0' 6001 6 api
##     docker run --hostname webserver-api --name webserver -d jeff1evesque/ml-webserver:0.7 '0.0.0.0' 5001 6 web
##
RUN $PUPPET apply -e "class { webserver: \
    run => false, \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
WORKDIR $ROOT_PROJECT
ENTRYPOINT ['/bin/sh', '-c', './entrypoint']
