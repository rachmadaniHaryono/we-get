"""
Copyright (c) 2016 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying permission
"""

import sys
from we_get.core.we_get import WG
from we_get.core.utils import msg_error
from we_get.core.utils import msg_err_trace


def main():
    we_get = WG()
    we_get.parse_arguments()
    try:
        we_get.start()
    except (EOFError, KeyboardInterrupt):
        msg_error("[KeyboardInterrupt]", True)
