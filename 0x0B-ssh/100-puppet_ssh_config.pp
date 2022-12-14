# set up your client SSH configuration file so that you can
# connect to a server without typing a password
# use: sudo puppet apply 100-puppet_ssh_config.pp

file_line { 'Identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'no password':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
