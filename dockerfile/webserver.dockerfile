FROM jeff1evesque/ml-sklearn:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## ensure directory
RUN mkdir -p $ROOT_PROJECT/interface $ROOT_PROJECT/hiera $ROOT_PUPPET/brain $ROOT_PUPPET/test

## copy files into container
COPY app.py factory.py __init__.py $ROOT_PROJECT/
COPY log $ROOT_PROJECT/log
COPY interface $ROOT_PROJECT/interface
COPY hiera $ROOT_PROJECT/hiera
COPY brain $ROOT_PROJECT/brain
COPY test/backend $ROOT_PROJECT/test/backend
COPY test/live_server $ROOT_PROJECT/test/live_server
COPY puppet/environment/$ENVIRONMENT/modules/webserver $ROOT_PUPPET/code/modules/webserver

##
## provision with puppet: either build a web, or api webserver image.
##
##     docker build -f webserver.dockerfile -t jeff1evesque/ml-webserver:0.7 .
##
RUN apt-get update && $PUPPET apply -e "class { webserver: \
    run      => false, \
    platform => 'development', \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

##
## executed everytime container starts
##
##     docker run --hostname webserver-api --name webserver-api -d jeff1evesque/ml-webserver:0.7 api 0.0.0.0 6001 6
##     docker run --hostname webserver-web --name webserver-web -d jeff1evesque/ml-webserver:0.7 web 0.0.0.0 5001 6
##     docker run\
##         --name webserver\
##         --net=app_nw\
##         -v "${PROJECT_ROOT}/app.py:/var/machine-learning/app.py"\
##         -v "${PROJECT_ROOT}/factory.py:/var/machine-learning/factory.py"\
##         -v "${PROJECT_ROOT}/__init__.py:/var/machine-learning/__init__.py"\
##         -v "${PROJECT_ROOT}/log:/var/machine-learning/log"\
##         -v "${PROJECT_ROOT}/interface:/var/machine-learning/interface"\
##         -v "${PROJECT_ROOT}/hiera:/var/machine-learning/hiera"\
##         -v "${PROJECT_ROOT}/brain:/var/machine-learning/brain"\
##         -v "${PROJECT_ROOT}/test:/var/machine-learning/test"\
##         -d jeff1evesque/ml-webserver:0.7\
##         test | sudo tee pytest.log
##
WORKDIR $ROOT_PROJECT
ENTRYPOINT ["/bin/bash", "./entrypoint"]
