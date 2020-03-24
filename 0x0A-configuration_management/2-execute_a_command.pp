# Using Puppet, kill a process named killmenow.
exec {'killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
  path     => '/usr/bin',
}
