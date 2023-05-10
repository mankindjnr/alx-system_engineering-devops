#  find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet
# (instead of using Bash as you were previously doing).

$path = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${path}",
  path    => ['/bin','/usr/bin']
}
