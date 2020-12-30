#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import typing
import xml.etree.ElementTree as ET
from urllib.parse import parse_qs, urlencode, urlparse

import aiohttp

from we_get.core.module import Module


async def get_raw_data(urls):
    async with aiohttp.ClientSession() as session:
        xmls = []
        for url in urls:
            async with session.get(url) as response:
                xmls.append(await response.text())
    return xmls


class JackettRss(object):
    """ Jackett rss module for we-get."""

    def __init__(self, pargs, urls: typing.Optional[typing.List[str]] = None):
        self.links = None
        self.pargs = pargs
        self.action = None
        self.search_query = None
        self.module = Module()
        self.parse_pargs()
        self.items = dict()
        self.urls = urls or []

    def parse_pargs(self):
        for opt in self.pargs:
            if opt == "--search":
                self.action = "search"
                self.search_query = self.pargs[opt][0]

    def _parse_data(self, data: typing.List[str]):
        for item in data:
            root = ET.fromstring(item)
            try:
                root_items = filter(lambda x: x.tag == "item", root[0])
            except IndexError:
                continue
            label = next(filter(lambda x: x.tag == "title", root[0])).text
            for subitem in root_items:
                title = next(filter(lambda x: x.tag == "title", subitem)).text
                seeds = int(
                    next(
                        filter(lambda x: x.attrib.get("name", "") == "seeders", subitem)
                    ).attrib.get("value", "0")
                )
                leeches = int(
                    next(
                        filter(lambda x: x.attrib.get("name", "") == "peers", subitem)
                    ).attrib.get("value", "0")
                )
                link = next(filter(lambda x: x.tag == "link", subitem)).text
                self.items.update(
                    {
                        title: {
                            "seeds": seeds,
                            "leeches": leeches,
                            "link": link,
                            "label": label,
                        }
                    }
                )

    def get_search_url(self, base_url, query):
        purl = urlparse(base_url)
        q_dict = parse_qs(purl.query)
        q_dict["q"] = [query]
        return purl._replace(query=urlencode(q_dict, doseq=True)).geturl()

    def search(self):
        if not self.urls:
            return self.items
        search_urls = map(
            lambda x: self.get_search_url(x, self.search_query), self.urls
        )
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(get_raw_data(search_urls))
        self._parse_data(data)
        return self.items

    def list(self):
        if not self.urls:
            return self.items
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(get_raw_data(self.urls))
        self._parse_data(data)
        return self.items


def main(pargs, urls: typing.Optional[typing.List[str]] = None):
    run = JackettRss(pargs, urls)
    if run.action == "search":
        return run.search()
    elif run.action == "search":
        return run.search()
