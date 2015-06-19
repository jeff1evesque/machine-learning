require 'spec_helper_acceptance'

describe 'nodejs class:', :unless => UNSUPPORTED_PLATFORMS.include?(fact('osfamily')) do
  it 'should run successfully' do
    pp = <<-EOS
    class { 'nodejs': }
    if $::osfamily == 'RedHat' and $::operatingsystemrelease =~ /^5\.(\d+)/ {
      class { 'epel': }
      Class['epel'] -> Class['nodejs']
    }
    EOS

    apply_manifest(pp, :catch_failures => true)
    apply_manifest(pp, :catch_changes => true)
  end
end
