Changelog
=========
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog<http://keepachangelog.com/en/1.0.0/>`_
and this project adheres to `Semantic Versioning<http://semver.org/spec/v2.0.0.html>`_.

1.1.3 - 2022-03-05
------------------

New
~~~

- documentation on how to install the program
- module limetorrents and il corsaro nero
- module the_pirate_bay size data
- pre commit config for contributor

Changes
~~~~~~~

- replace setup.py and requirements-dev.txt with pyproject.toml
- replace urllib with requests

Fix
~~~

- handle HTTPError and URLError
- github action flake8 test

1.1.2 - 2020-11-30
------------------

New
~~~

- include `__main__.py`

1.1.1 - 2020-11-20
------------------

New
~~~

- user status for pirate bay
- argv for arguments
- pby use api

Changes
~~~~~~~

- target parameter default to all


1.1.0 - 2018-07-08
------------------

Fixed
~~~~~

- prompt_toolkit upgrade

1.0.0 - 2017-04-26
------------------

New
~~~

- Added .gitignore. [Levi Sabah]
- Added __init__.py. [Levi Sabah]
- Added Changelog. [rachmadaniHaryono]
- Added exception to setup.cfg. [rachmadaniHaryono]
- Added installation via pip from git, thanks to @rachmadaniHaryono.  [Levi Sabah]
- Added python dependencies. [Levi Sabah]
- Added README.rst. [Levi Sabah]
- Added setup.py. [Levi Sabah]
- Added useragents.txt. [Levi Sabah]
- Core/commands.py: lower case commands help. [Levi Sabah]
- Core/commands.py: shell commands. [Levi Sabah]
- Core/completer.py: completer hook for prompt_toolkit. [Levi Sabah]
- Core/module.py: API for modules/ [Levi Sabah]
- Core/shell.py: main prompt using prompt_toolkit. [Levi Sabah]
- Core/style.py: style for core/shell.py. [Levi Sabah]
- Core/utils.py: helper functions. [Levi Sabah]
- Core/we_get.py: main we-get class. [Levi Sabah]
- Create LICENSE. [0xl3vi]
- Modules/1337x.py: module for 1337x. [Levi Sabah]
- Modules/eztv.py: module for eztv. [Levi Sabah]
- Modules/thepiratebay.py: module for thepiratebay. [Levi Sabah]
- Modules/yts.py: module for yts. [Levi Sabah]
- README.rst: Added options help and usage examples. [Levi Sabah]
- README.rst: added supported websites. [Levi Sabah]
- Tests/fake_shell.py: small testing shell for we-get. [Levi Sabah]
- Tests/test_arguments.py: test command line arguments with docopt.  [Levi Sabah]
- Travis yaml. [rachmadaniHaryono]

Changes
~~~~~~~

- Setup.py: Version to follow semantic versioning. [rachmadaniHaryono]
- Set max line and exclude setup.py. [rachmadaniHaryono]
- Format everything in accordance with PEP8. [Hendrikto]

Fix
~~~

- Core/we_get.py: Fix cut item and sorting (#5). [rachmadaniHaryono]
- Install command in travis. [rachmadaniHaryono]
