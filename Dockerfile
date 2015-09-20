FROM ubuntu:14.04

## install git, and wget
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install wget -y

## install openssh
RUN apt-get install openssh-client

## private github deploy ssh-key (readonly)
RUN mkdir ~/.ssh && chmod 700 ~/.ssh
RUN eval $(ssh-agent -s)
RUN ssh-agent -s
RUN printf '-----BEGIN RSA PRIVATE KEY-----\n\
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\n\
-----END RSA PRIVATE KEY-----'\
>> ~/.ssh/id_rsa

## add private github deploy key in ssh config
RUN printf 'Host machine-learning github.com\n\
    Hostname github.com\n\
    IdentityFile ~/.ssh/id_rsa'\
>> ~/.ssh/config

## test ssh connection to github
RUN ssh -T git@github.com

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
RUN dpkg -i puppetlabs-release-trusty.deb
RUN apt-get update -y

## install r10k
RUN apt-get install rubygems-integration -y
RUN gem install r10k

## clone repository: allow puppet manifests to run (below)
RUN git clone https://jeff1evesque@github.com/jeff1evesque/machine-learning.git /var/machine-learning

## install puppet modules using puppetfile with r10k
RUN PUPPETFILE=/var/machine-learning/puppet/Puppetfile PUPPETFILE_DIR=/var/machine-learning/puppet/modules/ r10k puppetfile install

## provision with puppet
RUN for x in $(find . -name '/var/machine-learning/puppet/manifests/*.pp'); do puppet apply $x; done;
