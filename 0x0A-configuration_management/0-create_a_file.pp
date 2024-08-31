# create file in tmp
file {
owner 	=> www-data,
permission => 0744,
group 	=> www-data,
content => I love Puppet
}
