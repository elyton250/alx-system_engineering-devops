# Kills a process named 'killmenow' using Puppet cm
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
