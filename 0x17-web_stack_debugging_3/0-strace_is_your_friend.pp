# They say strace is our friends
exec { 'remove typo':
    cwd     => '/var/www/html',
    command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}