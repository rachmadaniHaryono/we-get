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
       '--link' : 'Show .torrent/magnet link', 
       '--seeds' : 'Show number of seeds', 
       '--leeches' : 'Show number of leeches for this torrent',
       '--target' : 'Show torrent target'
     }
   },
  'list' : {
    'help' : 'List torrents',
    'usage' : '',
    'required_argument' : False,
    'opts' : {}
  },
  'exit' : {
    'help' : 'Exit the shell',
    'usage' : '',
    'required_argument' : False,
    'opts': {}
  },
  'help' : {
    'help' : 'Show help message',
    'usage' : '',
    'required_argument' : False,
    'opts' : {}
  }
}


