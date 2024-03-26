#!/usr/bin/env bash
# Using puppet to connect to server without password

file {'/etc/ssh/ssh_config':
  ensure  => present,
}

file_line {'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication',
}

file_line {'Declare Identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentitiFile',
}
