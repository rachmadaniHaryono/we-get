"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying.
"""

import re
import sys
from glob import glob
from os import sep
from random import choice
from typing import Dict, Optional

from colorama import Fore, Style
from colorama import init as colorama_init

from we_get import __file__ as p

colorama_init(autoreset=True)

# supported color from colorama 0.4.3
#  BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
COLORS = {
    "black": Fore.BLACK,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "green": Fore.GREEN,
    "magenta": Fore.MAGENTA,
    "red": Fore.RED,
    "white": Fore.WHITE,
    "yellow": Fore.YELLOW,
}
ITEM_COLOR_SET = {
    'leeches': 'red',
    'target': 'green',
    'item': 'white',
    'seeds': 'green',
    'user_status': 'green',
    'user_status_vip': 'magenta'
}

def format_help(doc, errmsg):
    """ format_help: fix help message.
    """
    for line in doc.split("\n"):
        if "options:" in line or "Options" in line:
            line = color("yellow", line)
        elif re.findall(r'<(\w+)>', line):
            value = re.findall(r'<(\w+)>', line)[0]
            line = line.replace('<%s>' % (value),
                                "[%s]" % (color("cyan", value)))
            line = line.replace('=', ' ')
        print(line)
    if errmsg:
        msg_error("%s" % (errmsg), True)
    sys.stdout.write("Copyright (c) 2016 by 0xl3vi <0xl3vi@gmail.com>.\n")
    sys.stdout.write(
        "Full documentation at: <http://github.com/0xl3vi/we-get>\n"
    )


def printc(color, text):
    """printc: print colors
      @color
      @text
    """
    for x in COLORS:
        if x == color:
            sys.stdout.write("%s%s%s\n" % (COLORS[x], text, Style.RESET_ALL))


def printc_raw(color, text):
    """printc_raw: print colors without new line
    @color
    @text
    """
    for x in COLORS:
        if x == color:
            sys.stdout.write("%s%s%s" % (COLORS[x], text, Style.RESET_ALL))


def msg_err_trace(exit=False):
    """ msg_err_trace: print dump of error.
    """
    msg_error("%s\n# %s\n# %s" % (
        sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
    ), exit)


""" msg_fetching: Show message hen fetching data from @target."
      @target - name
"""


def msg_fetching(target):
    sys.stdout.write("%s#%s Fetching data from %s\'%s'%s ...\r" % (
        Fore.YELLOW, Style.RESET_ALL,
        Fore.BLUE, target, Style.RESET_ALL
    ))


def color(color, msg):
    """ color: return colored text using colorama.
       @color - Fore.color
       @msg - string.
    """
    for x in COLORS:
        if x == color:
            return "%s%s%s" % (COLORS[x], msg, Style.RESET_ALL)


def msg_error(msg, exit):
    """ msg_error : error message.
      @msg: string.
      @exit  : exit?
    """
    sys.stdout.write("%s# error: %s\n" % (Fore.RED, msg))
    if exit:
        sys.exit(1)


def msg_info(msg):
    """ msg_info: info message.
      @msg - string.
    """
    sys.stdout.write("%s# %s\n" % (Fore.BLUE, msg))


def msg_item(
        item: str,
        items: Dict[str, str],
        item_color: Optional[Dict[str, str]] = None
):
    """ msg_item: print item.
      @item - name.
      @items - item status (leeches, seed, target, etc)
      @item_color - item color.
    """
    cset = ITEM_COLOR_SET.copy()
    if item_color is not None:
        cset.update(item_color)
    leeches = items['leeches']
    seeds = items['seeds']
    target = items['target']
    user_status = items.get('user_status', None)
    user_status_text = ''
    if user_status and user_status is not None:
        if user_status == 'vip':
            user_status_text = color(cset['user_status_vip'], user_status)
        else:
            color(cset['user_status'], user_status)

    text = (
        "%s %s [%s/%s] %s" % (
            color(cset['target'], target),
            color(cset['item'], item),
            color(cset['seeds'], seeds),
            color(cset['leeches'], leeches),
            user_status_text
        )
    )
    sys.stdout.write(text + '\n')


def mkpath(path):
    """ mkpath - create cross platfrom path.
      @path - path .

      by default we are using / for sep.
      mkpath() will replace the default sep with os.sep.
      this way we will create cross platfrom path.
    """
    return path.replace('/', sep)


def pkgpath():
    """ pkgpath: return the location of the installed packages.
    """
    x = p.split(sep)
    x.pop(-1)  # Remove __init__.py
    return sep.join(x)


def random_user_agent():
    """ rand_user_agent - return random user agent from txt/useragents.txt
    """
    agents_path = mkpath("%s/txt/useragents.txt" % (pkgpath()))
    try:
        data = open(agents_path, "r").readlines()
        return choice(data)[:-1]
    except IOError:
        msg_error(
            "Cannot open: %s - to read user agents." % (agents_path), True
        )


def list_wg_modules():
    """ list_wg_modules - list all modules from modules/.
    """
    modules = list()
    path = mkpath("%s/modules/*.py" % (pkgpath()))
    for module in glob("%s" % (path)):
        if "__init__" not in module:
            module = module.split("%s" % (sep))[-1].split(".")[0]
            modules.append(module)
    return modules
