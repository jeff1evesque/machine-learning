require 'spec_helper'
describe 'apt::conf', :type => :define do
  let :pre_condition do
    'class { "apt": }'
  end
  let(:facts) { { :lsbdistid => 'Debian', :osfamily => 'Debian', :lsbdistcodename => 'wheezy', :puppetversion   => Puppet.version, } }
  let :title do
    'norecommends'
  end

  describe "when creating an apt preference" do
    let :params do
      {
        :priority => '00',
        :content  => "Apt::Install-Recommends 0;\nApt::AutoRemove::InstallRecommends 1;\n"
      }
    end

    let :filename do
      "/etc/apt/apt.conf.d/00norecommends"
    end

    it { is_expected.to contain_file(filename).with({
          'ensure'    => 'present',
          'content'   => /Apt::Install-Recommends 0;\nApt::AutoRemove::InstallRecommends 1;/,
          'owner'     => 'root',
          'group'     => 'root',
          'mode'      => '0644',
        })
      }
  end

  describe "when creating a preference without content" do
    let :params do
      {
        :priority => '00',
      }
    end

    it 'fails' do
      expect { subject.call } .to raise_error(/pass in content/)
    end
  end

  describe "when removing an apt preference" do
    let :params do
      {
        :ensure   => 'absent',
        :priority => '00',
      }
    end

    let :filename do
      "/etc/apt/apt.conf.d/00norecommends"
    end

    it { is_expected.to contain_file(filename).with({
        'ensure'    => 'absent',
        'owner'     => 'root',
        'group'     => 'root',
        'mode'      => '0644',
      })
    }
  end
end
