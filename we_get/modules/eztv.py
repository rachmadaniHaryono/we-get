"""
Copyright (c) 2016 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.module import Module
import re

BASE_URL = "http://eztv.ag"
SEARCH_LOC = "/search/%s/"
LIST_LOC = "/"


class eztv(object):
    """ eztv module for we-get.
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
        items = re.findall(
            r'<tr name=\"hover\" class=\"forum_header_border\">(.*?)</tr>',
            data,
        )
        seeds = None
        leeches = None
        magnet = None

        for item in items:
            if "magnet:" in item:
                try:
                    seeds = re.findall(
                        r'<font color=\"green\">(.*?)</font>',
                        item,
                    )[0]
                    # In case seeds will be 1,212
                    seeds = seeds.replace(',', '')
                except IndexError:
                    seeds = '0'
                # EZTv will not return lecches ):
                leeches = "?"
                magnet = re.findall(r'href=[\'"]?([^\'">]+)', item)[2]
                name = self.module.fix_name(self.module.magnet2name(magnet))
                self.items.update({
                    name: {'seeds': seeds, 'leeches': leeches, 'link': magnet}
                })

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
    run = eztv(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
