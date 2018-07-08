"""
Copyright (c) 2016-2018 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.module import Module
import re

BASE_URL = "http://1337x.to"
SEARCH_LOC = "/search/%s/1/"
LIST_LOC = "/top-100"


class leetx(object):
    """ 1337x module for we-get.
    """

    def __init__(self, pargs):
        self.links = None
        self.pargs = pargs
        self.action = None
        self.search_query = None
        self.module = Module()
        self.parse_pargs()
        self.items = dict()
        self.results = 10  # Limit the results to avoid blocking.

    def parse_pargs(self):
        for opt in self.pargs:
            if opt == "--search":
                self.action = "search"
                self.search_query = self.pargs[opt][0]
            elif opt == "--list":
                self.action = "list"

    def set_item(self, link):
        url = "%s%s" % (BASE_URL, link)
        magnet = None
        data = self.module.http_get_request(url)
        links = re.findall(r'href=[\'"]?([^\'">]+)', data)
        seeders = re.findall(r'<span class=\"seeds\">(.*?)</span>', data)[0]
        leechers = re.findall(r'<span class=\"leeches\">(.*?)</span>', data)[0]
        item = dict()
        name = None

        for link in links:
            if "magnet" in link:
                magnet = link
                break
        name = self.module.fix_name(self.module.magnet2name(magnet))
        item.update(
            {name: {'seeds': seeders, 'leeches': leechers, 'link': magnet}}
        )
        return item

    def search(self):
        url = "%s%s" % (BASE_URL, SEARCH_LOC % (self.search_query))
        data = self.module.http_get_request(url)
        links = re.findall(r'href=[\'"]?([^\'">]+)', data)
        results = 0

        for link in links:
            if "/torrent/" in link:
                if results == self.results:
                    break
                item = self.set_item(link)
                self.items.update(item)
                results += 1
        return self.items

    def list(self):
        url = "%s%s" % (BASE_URL, LIST_LOC)
        data = self.module.http_get_request(url)
        links = re.findall(r'href=[\'"]?([^\'">]+)', data)
        results = 0

        for link in links:
            if "/torrent/" in link:
                if results == self.results:
                    break
                item = self.set_item(link)
                self.items.update(item)
                results += 1
        return self.items


def main(pargs):
    run = leetx(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
