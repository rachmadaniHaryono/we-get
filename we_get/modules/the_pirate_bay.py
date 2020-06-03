"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.module import Module
import re

BASE_URL = "https://www1.thepiratebay3.to"
SEARCH_LOC = "/search/%s/1/7/0"
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
        items = re.findall(
            r'<div class=\"detName\">(.*?)<div class=\"detName\">', data)
        seeds = None
        leeches = None
        magnet = None

        for item in items:
            seeds, leeches = re.findall(
                r'<td align=\"right\">(\d+)</td>', item
            )
            magnet = re.findall(r'href=[\'"]?([^\'">]+)', item)[1]
            user_status = re.findall(r'<img.+title="(Trusted|VIP)"', item)
            try:
                user_status = user_status[0].lower()
            except IndexError:
                user_status = None
            name = self.module.fix_name(self.module.magnet2name(magnet))
            self.items.update({
                name: {
                    'seeds': seeds, 'leeches': leeches,
                    'link': magnet, 'user_status': user_status}
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
    run = the_pirate_bay(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
