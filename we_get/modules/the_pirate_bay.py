"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""
from bs4 import BeautifulSoup

from we_get.core.module import Module
import re

BASE_URL = "https://www1.thepiratebay3.to"
SEARCH_LOC = "/s/?q="
LIST_LOC = "/top/all"
SFW_FILTER = "&audio=on&video=on&apps=on&games=on&other=on&category=0"

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
        self.filter = ""

    def parse_pargs(self):
        for opt in self.pargs:
            if opt == "--search":
                self.action = "search"
                self.search_query = self.pargs[opt][0].replace(' ', '-')
            elif opt == "--list":
                self.action = "list"
            if opt == "--sfw":
                self.filter = SFW_FILTER

    def _parse_data(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        items = soup.find_all("tr")
        seeds = None
        leeches = None
        magnet = None

        for item in items:
            cols = item.find_all("td")
            if len(cols) > 1:
                name = cols[1].a.contents[0]
                magnet = cols[3].a['href']
                seeds = cols[5].contents[0]
                leeches = cols[6].contents[0]
                user_status = None
                self.items.update({
                    name: {
                        'seeds': seeds, 'leeches': leeches,
                        'link': magnet, 'user_status': user_status}
                })

    def search(self):
        url = f"{BASE_URL}{SEARCH_LOC}{self.search_query}{self.filter}"
        data = self.module.http_get_request(url)
        self._parse_data(data)
        return self.items

    def list(self):
        url = f"{BASE_URL}{LIST_LOC}"
        data = self.module.http_get_request(url)
        self._parse_data(data)
        return self.items


def main(pargs):
    run = the_pirate_bay(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
