# Using Puppet, install a package called puppet-lint.
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
