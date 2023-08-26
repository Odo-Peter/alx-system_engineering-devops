# kills a process in the shell terminal

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  }