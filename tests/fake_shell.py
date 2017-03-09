#!/usr/bin/env python
""" test_module.py - fake we_get shell. """

from we_get.core.shell import Shell

items = dict()
x = {'Some.Cool.Torrent1' : {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent2' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent3' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent4' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent5' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent6' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent7' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 },
     'Some.Cool.Torrent8' :  {'target' : 'test', 'link'  : 'magnet://link', 'seeds' : 7000, 'leeches' : 0 }
}
items.update(x)

def main():
  s = Shell()
  s.shell(x, {'--search' : ['test'] })

if __name__ == '__main__':
  main()
