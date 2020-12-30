#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pathlib

import pytest

from we_get.modules import jackett_rss

XML1_PATH = pathlib.Path(__file__).parent / "test1.xml"


def test_search():
    urls = [
        "http://127.0.0.1:9117/api/v2.0/indexers/linuxtracker/results/torznab/api?apikey=lbwgkgyej6sbt2ubch1jn3615purap0a&t=search&cat=&q="
    ]
    obj = jackett_rss.JackettRss({"--search": ["ubuntu"]}, urls)
    res = obj.search()


@pytest.mark.skipif(not XML1_PATH.is_file(), reason="test xml not exist")
def test_parse_data():
    json_path = pathlib.Path(__file__).parent / "test1.xml.json"
    with XML1_PATH.open() as f:
        data = [f.read()]
    with json_path.open() as f:
        exp_data = json.load(f)
    obj = jackett_rss.JackettRss([])
    obj._parse_data(data)
    assert obj.items == exp_data


def test_get_search_url():
    base_url = "http://127.0.0.1:9117/api/v2.0/indexers/linuxtracker/results/torznab/api?apikey=lbwgkgyej6sbt2ubch1jn3615purap0a&t=search&cat=&q="
    exp_url = "http://127.0.0.1:9117/api/v2.0/indexers/linuxtracker/results/torznab/api?apikey=lbwgkgyej6sbt2ubch1jn3615purap0a&t=search&q=ubuntu"
    obj = jackett_rss.JackettRss([])
    assert obj.get_search_url(base_url, "ubuntu") == exp_url
