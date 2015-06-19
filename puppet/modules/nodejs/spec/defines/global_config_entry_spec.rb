require 'spec_helper'

describe 'nodejs::npm::global_config_entry', :type => :define do

  let :pre_condition do
    'class { "nodejs": }'
  end

  context "when run on Debian Wheezy" do

    let :facts do
      {
        :lsbdistcodename        => 'Wheezy',
        :lsbdistid              => 'Debian',
        :operatingsystem        => 'Debian',
        :operatingsystemrelease => '8.0',
        :osfamily               => 'Debian',
      }
    end

    context 'with name set to proxy and value set to proxy.domain' do
      let (:title) { 'proxy' }
      let (:params) { { :value => 'proxy.domain' } }

      it 'npm config set proxy proxy.domain should be executed' do
        should contain_exec('npm_config present proxy').with({
          'command' => '/usr/bin/npm config set proxy proxy.domain --global',
        })
      end
    end

    context 'with name set to https-proxy and value set to proxy.domain' do
      let (:title) { 'https-proxy' }
      let (:params) { { :value => 'proxy.domain' } }

      it 'npm config set https-proxy proxy.domain should be executed' do
        should contain_exec('npm_config present https-proxy').with({
          'command' => '/usr/bin/npm config set https-proxy proxy.domain --global',
        })
      end
    end

    context 'with name set to color and ensure set to absent' do
      let (:title) { 'color' }
      let (:params) { { :ensure => 'absent' } }

      it 'npm config delete color should be executed' do
        should contain_exec('npm_config absent color').with({
          'command' => '/usr/bin/npm config delete color',
        })
      end
    end

    context 'with name set to foo and ensure set to an invalid value' do
      let (:title) { 'foo' }
      let (:params) { { :ensure => 'invalid_value' } }

      it 'should fail' do
        expect { catalogue }.to raise_error(Puppet::Error, /nodejs::npm::global_config_entry : Ensure parameter must be present or absent/)
      end
    end
  end
end
