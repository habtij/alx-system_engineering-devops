# Fix bad "phpp" extensions to "php" in Wordpress settings file
exec {'fix type in filename':
  command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider=> shell,
}
