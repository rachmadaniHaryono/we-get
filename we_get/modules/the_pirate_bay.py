"""
Copyright (c) 2016 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.module import Module
import re

BASE_URL = "https://thepiratebay.org"
SEARCH_LOC = "/search/%s/0/99/0"
LIST_LOC = "/top/all"

class the_pirate_bay(object):
  """ the_pirate_bay module for we-get.
  """
  def __init__(self, pargs):
    self.links = None
    self.pargs = pargs
    self.action = None
    self.search_query = None
    self.module = Module()
    self.parse_pargs()
    self.items = dict()
  
  def parse_pargs(self):
    for opt in self.pargs:
      if opt == "--search":
        self.action = "search"
        self.search_query = self.pargs[opt][0].replace(' ', '-')
      elif opt == "--list":
        self.action = "list"

  def _parse_data(self, data):
    data = data.replace('\t', '').replace('\n', '')
    items = re.findall(r'<div class=\"detName\">(.*?)<div class=\"detName\">', data)
    seeds = None
    leeches = None
    magnet  = None

    for item in items:
      seeds, leeches = re.findall(r'<td align=\"right\">(\d+)</td>', item)
      magnet = re.findall(r'href=[\'"]?([^\'">]+)', item)[1]
      name = self.module.fix_name(self.module.magnet2name(magnet))
      self.items.update( { name : { 'seeds' : seeds, 'leeches' : leeches, 'link' : magnet} })

  def search(self):
    url = "%s%s" % (BASE_URL, SEARCH_LOC % (self.search_query))
    data = self.module.http_get_request(url)
    self._parse_data(data)
    return self.items

  def list(self):
    url = "%s%s" % (BASE_URL, LIST_LOC)
    data = self.module.http_get_request(url)
    self._parse_data(data)
    return self.items

def main(pargs):
  run = the_pirate_bay(pargs)
  if run.action == "list":
    return run.list()
  elif run.action == "search":
    return run.search()
