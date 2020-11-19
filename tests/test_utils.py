#!/usr/bin/env python
# -*- coding: utf-8 -*-
from we_get.core import utils


def test_msg_item():
    args = [
        'Ubuntu.MATE.16.04.2.[MATE][armhf][img.xz][Uzerus]',
        {
            'leeches': '2',
            'link': 'magnet:?xt=urn:btih:D0F23C109D8662A3FE9338F75839AF8D57E5D4A9'
            '&dn=Ubuntu+MATE+16.04.2+%5BMATE%5D%5Barmhf%5D%5Bimg.xz%5D%5BUzerus%5D',
            'seeds': '260',
            'target': '1337x'}
    ]
    utils.msg_item(*args)
