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
                        "size": humanbytes(row["size"]),
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

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)
