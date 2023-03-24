#creating a file in /tmp with file permisions, owner, group set
file { '/tmp/school':
  content  => "I love Puppet",
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
}
