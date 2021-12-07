we-get: command-line tool for searching torrents.
#################################################

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square   
    :target: https://github.com/rachmadaniHaryono/we-get/blob/master/LICENSE
    
    
.. image:: https://img.shields.io/aur/version/we-get-git.svg?maxAge=600
    :target: https://aur.archlinux.org/packages/we-get-git/

.. class:: head

    .. image:: https://raw.githubusercontent.com/rachmadaniHaryono/we-get/master/res/screenshot.png
        :alt: Main screenshot.
        :width: 100%
        :align: center



.. contents::
.. section-numbering::

Installation
============

.. install new python 3.10 from python website to mac
.. pip3 install beautifulsoup4 colorama docopt prompt-toolkit Pygments
run from the root folder

.. code-block:: bash

    $ sudo /usr/local/bin/python3 -d setup.py install


or with ``pip``

.. code-block:: bash

    $ pip3 install git+https://github.com/rachmadaniHaryono/we-get
    $ # or use --user flag to install in your home directory
    $ pip3 install --user git+https://github.com/rachmadaniHaryono/we-get


Dependencies
============

* `prompt_toolkit <https://github.com/jonathanslenders/python-prompt-toolkit>`_, `docopt <https://github.com/docopt/docopt>`_, `colorama <https://github.com/tartley/colorama>`_, `beautifulsoup4 <https://github.com/wention/BeautifulSoup4>`_

and `Python <https://www.python.org/>`_ 3.5 or above


Basic Usage
===========

.. code-block:: bash

    $ we-get --search "royal pains" --target  the_pirate_bay,1337x --filter "S01"

General options
---------------

============ =============
-h --help    Help message.
-v --version Show version.
============ =============

Options
-------

===================== =====================================================
-s --search=<text>    Search for a torrent.                                
-l --list             List top torrents from modules.                      
-t --target=<target>  Select module to use or 'all' [default: all].        
-L --links            Output results as links.                             
-J --json             Output results in JSON format.                       
-G --get-list         List targets (supported web-sites).                  
-f --filter=<str>     Match text or regular expression in the torrent name.
-n --results=<n>      Number of results to retrieve.                       
-S --sort-type=<type> Sort torrents by name/seeds [default: seeds].        
-c --config=<file>    Load config file.
-w --sfw              Restrict results to safe for work content (the_pirate_bay only)                                    
===================== =====================================================

Video options
-------------

================ ==================================================================
-q --quality=<q> Try to match quality for the torrent (720p,1080p, ...).           
-g --genre=<g>   Try to select video genre for the torrent (action, comedy, etc..).
================ ==================================================================


See also ``we-get --help``.

Python Module
-------------

.. code-block:: python

   >>> from we_get.core.we_get import WG
   >>> we_get = WG()
   >>> we_get.parse_arguments(['--search', 'ubuntu', '--target', 'all'])
   >>> res = we_get.start(api_mode=True)
   OrderedDict([
      (
         'Ubuntu.MATE.16.04.2.[MATE][armhf][img.xz][Uzerus]', {
            'seeds': '260',
            'leeches': '2',
            'link':
                'magnet:?xt=urn:btih:D0F23C109D8662A3FE9338F75839AF8D57E5D4A9'
                '&dn=Ubuntu+MATE+16.04.2+%5BMATE%5D%5Barmhf%5D%5Bimg.xz%5D%5BUzerus%5D'
                '&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce'
                '&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce'
                '&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce'
                '&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce',
            'target': '1337x'}
      ),
      ...
   ])

Older version can use `sys.argv` to input the arguments

.. code-block:: python

   >>> import sys
   >>> from we_get.core.we_get import WG
   >>> we_get = WG()
   >>> sys.argv[1:] = ['--search', 'ubuntu', '--target', 'all']
   >>> we_get.parse_arguments()
   >>> we_get.start(api_mode=True)
   ...


Supported websites
------------------

* 1337x
* thepiratebay
* eztv
* yts

and the list will grow.

Contributing
------------

Any collaboration is welcome!

If you want to write a module please see ``we_get/modules/``


Licence
-------

MIT: `LICENSE <https://github.com/rachmadaniHaryono/we-get/blob/master/LICENSE>`_.

Testing
=======

Dependencies
------------

* pytest
* pytest-flake8

Run tests with ``python -m pytest --flake8``.
