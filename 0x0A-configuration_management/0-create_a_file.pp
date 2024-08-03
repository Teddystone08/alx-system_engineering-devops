# create file in tmp
file {'/tmp/school':
ensure => 'school',
content => 'I love Puppet',
owner => 'www-data',
group => 'www-data',
mode => '0744' 
}
