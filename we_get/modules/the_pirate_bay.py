"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""
from we_get.core.module import Module
import urllib
import json


API_URL = "https://apibay.org"
API_SEARCH_LOC = "/q.php?q="
ALI_LIST_LOC = "/precompiled/data_top100_all.json"
API_SFW_FILTER = "&cat=100,200,300,400,600"
API_TRACKERS = "&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce"  # NOQA


class the_pirate_bay(object):
    """the_pirate_bay module for we-get."""

    def __init__(self, pargs):
        self.links = None
        self.pargs = pargs
        self.action = None
        self.search_query = None
        self.filter = ""
        self.module = Module()
        self.parse_pargs()
        self.items = dict()

    def parse_pargs(self):
        for opt in self.pargs:
            if opt == "--search":
                self.action = "search"
                self.search_query = self.pargs[opt][0].replace(" ", "-")
            elif opt == "--list":
                self.action = "list"
            if opt == "--sfw":
                self.filter = API_SFW_FILTER

    def generate_magnet(self, data):
        return f"magnet:?xt=urn:btih:{data['info_hash']}&dn={urllib.parse.quote(data['name'])}{API_TRACKERS}"  # NOQA

    def _parse_data(self, data):
        for row in json.loads(data):
            self.items.update(
                {
                    row["name"]: {
                        "seeds": row["seeders"],
                        "leeches": row["leechers"],
                        "link": self.generate_magnet(row),
                        "user_status": row["status"],
                    }
                }
            )

    def search(self):
        url = f"{API_URL}{API_SEARCH_LOC}{self.search_query}{self.filter}"
        data = self.module.http_get_request(url)
        self._parse_data(data)
        return self.items

    def list(self):
        url = f"{API_URL}{ALI_LIST_LOC}"
        data = self.module.http_get_request(url)
        self._parse_data(data)
        return self.items


def main(pargs):
    run = the_pirate_bay(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
