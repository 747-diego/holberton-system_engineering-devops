# Testing web server setup using Nginx
exec { 'TESTING Web Server':
  command  => 'sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
