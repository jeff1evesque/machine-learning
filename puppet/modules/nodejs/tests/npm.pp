include 'nodejs'

nodejs::npm { 'express|/tmp/npm':
  ensure  => '2.5.9',
}
