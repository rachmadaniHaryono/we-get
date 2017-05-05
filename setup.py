"""
Copyright (c) 2016 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying permission
"""


from setuptools import setup, find_packages
version = '0.1'

setup(
    name='we-get',
    version=version,
    description='Search torrents from the command-line',
    author='Levi Sabah',
    author_email='0xl3vi@gmail.com',
    license='MIT',
    keywords=['command line', 'torrent'],
    url='https://github.com/0xl3vi/we-get',
    packages=find_packages(),
    install_requires=['docopt', 'prompt_toolkit', 'colorama'],
    include_package_data=True,
    package_data={'we_get': ['txt/useragents.txt']},
    entry_points={'console_scripts': ['we-get=we_get:main']}
)
