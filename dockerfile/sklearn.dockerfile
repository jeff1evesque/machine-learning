FROM jeff1evesque/ml-base:0.8

## local variables
ENV ENVIRONMENT=docker\
    PUPPET=/opt/puppetlabs/bin/puppet\
    ROOT_PROJECT=/var/machine-learning\
    ROOT_PUPPET=/etc/puppetlabs\
    MODULES=$ROOT_PUPPET/code/modules\
    CONTRIB_MODULES=$ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY hiera $ROOT_PROJECT/hiera
COPY puppet/environment/$ENVIRONMENT/modules/sklearn $ROOT_PUPPET/code/modules/sklearn

## provision with puppet
RUN $PUPPET apply -e 'class { sklearn: }' --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
