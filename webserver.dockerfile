FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY log /var/machine-learning/log
COPY interface /var/machine-learning/interface
COPY hiera /var/machine-learning/hiera
COPY brain /var/machine-learning/brain
COPY test /var/machine-learning/test
COPY app.py /var/machine-learning/app.py
COPY factory.py /var/machine-learning/factory.py
COPY __init__.py /var/machine-learning/__init__.py
COPY puppet/environment/$ENVIRONMENT/modules/sklearn $ROOT_PUPPET/code/modules/sklearn
COPY puppet/environment/$ENVIRONMENT/modules/webserver $ROOT_PUPPET/code/modules/webserver

## install pytest-cov
RUN pip install pytest-cov==2.4.0

## provision with puppet
RUN $PUPPET apply $MODULES/sklearn/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet
RUN $PUPPET apply $MODULES/webserver/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
WORKDIR /var/machine-learning
ENTRYPOINT ["python", "app.py"]