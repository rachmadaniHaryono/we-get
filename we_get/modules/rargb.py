"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.module import Module
import json

BASE_URL = "https://www.rarbg.to/torrents.php"
SEARCH_LOC = "/api/v2/list_movies.json?query_term=%s&quality%s&genre=%s"
LIST_LOC = "/api/v2/list_movies.json?quality=%s&genre=%s"


class rargb(object):
    """ rargb module using the JSON API.
    """

    def __init__(self, pargs):
        self.links = None
        self.pargs = pargs
        self.action = None
        self.quality = "720p"
        self.genre = "all"
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
            elif opt == "--quality":
                self.quality = self.pargs[opt][0]
            elif opt == "--genre":
                self.genre = self.pargs[opt][0]

    def search(self):
        url = "%s%s" % (
            BASE_URL,
            SEARCH_LOC % (self.search_query, self.quality, self.genre)
        )
        data = json.loads(self.module.http_get_request(url))
        try:
            api = data['data']['movies']
        except KeyError:
            return self.items
        for movie in api:
            name = self.module.fix_name(movie['title'])
            seeds = movie['torrents'][0]['seeds']
            leeches = movie['torrents'][0]['peers']
            link = movie['torrents'][0]['url']
            self.items.update({
                name: {'seeds': seeds, 'leeches': leeches, 'link': link}
            })
        return self.items

    def list(self):
        url = "%s%s" % (BASE_URL, LIST_LOC % (self.quality, self.genre))
        try:
            data = json.loads(self.module.http_get_request(url))
        except json.decoder.JSONDecodeError:
            return self.items
        try:
            api = data['data']['movies']
        except KeyError:
            return self.items
        for movie in api:
            torrent_name = self.module.fix_name(movie['title'])
            seeds = movie['torrents'][0]['seeds']
            leeches = movie['torrents'][0]['peers']
            link = movie['torrents'][0]['url']
            self.items.update({torrent_name: {'leeches': leeches,
                                              'seeds': seeds, 'link': link}})
        return self.items


def main(pargs):
    run = rargb(pargs)
    if run.action == "list":
        return run.list()
    elif run.action == "search":
        return run.search()
