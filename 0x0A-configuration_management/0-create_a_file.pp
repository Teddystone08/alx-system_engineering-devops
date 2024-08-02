file { 'temp':
  ensure  => present,
  path    => '/tmp/schoo'
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
