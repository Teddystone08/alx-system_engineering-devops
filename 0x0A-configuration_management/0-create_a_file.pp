# create file in tmp
file {/tmp/school:
owner => www-data,
permission => '0744',
group => www-data,
content => 'I love Puppet'
}
