"""
Copyright (c) 2016 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying.
"""

# COMMANDS - built in we-get shell commands.
COMMANDS = {
  'show' : { 
     'help'  : 'Show torrent',
     'usage' : '[torrent/regex] [options]',  
     'required_argument' : True,
     'opts' : {
       '--link' : 'show .torrent/magnet link',
       '--seeds' : 'show number of seeds',
       '--leeches' : 'show number of leeches for this torrent',
       '--target' : 'show torrent target'
     }
   },
  'list' : {
    'help' : 'list torrents',
    'usage' : '',
    'required_argument' : False,
    'opts' : {}
  },
  'exit' : {
    'help' : 'exit the shell',
    'usage' : '',
    'required_argument' : False,
    'opts': {}
  },
  'help' : {
    'help' : 'show help message',
    'usage' : '',
    'required_argument' : False,
    'opts' : {}
  }
}


