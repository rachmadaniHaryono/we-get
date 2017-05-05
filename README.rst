we-get: command-line tool for searching torrents.
#################################################

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square   :target:

.. class:: head

    .. image:: https://raw.githubusercontent.com/rachmadaniHaryono/we-get/master/res/screenshot.png
        :alt: Main screenshot.
        :width: 100%
        :align: center



.. contents::
.. section-numbering::

Installation
============

run from the root folder

.. code-block:: bash

    $ sudo python setup.py install


or with ``pip``

.. code-block:: bash

    $ sudo pip install git+https://github.com/0xl3vi/we-get


Dependencies
============

* `prompt_toolkit <https://github.com/jonathanslenders/python-prompt-toolkit>`_, `docopt <https://github.com/docopt/docopt>`_, `colorama <https://github.com/tartley/colorama>`_

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
-t --target=<target>  Select module to use or 'all'.                       
-L --links            Output results as links.                             
-J --json             Output results in JSON format.                       
-G --get-list         List targets (supported web-sites).                  
-f --filter=<str>     Match text or regular expression in the torrent name.
-n --results=<n>      Number of results to retrieve.                       
-S --sort-type=<type> Sort torrents by name/seeds (default: seeds).        
===================== =====================================================

Video options
-------------

================ ==================================================================
-q --quality=<q> Try to match quality for the torrent (720p,1080p, ...).           
-g --genre=<g>   Try to select video genre for the torrent (action, comedy, etc..).
================ ==================================================================



See also ``we-get --help``.

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

MIT: `LICENSE <https://github.com/0xl3vi/we-get/blob/master/LICENSE>`_.

Testing
=======

Dependencies
------------

* pytest
* pytest-flake8

Run tests with ``python -m pytest --flake8``.
