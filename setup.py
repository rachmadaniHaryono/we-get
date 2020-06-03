"""
Copyright (c) 2016-2020 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""


from setuptools import setup, find_packages
version = '1.1.0'

setup(
    name='we-get',
    version=version,
    description='Search torrents from the command-line',
    author='Levi Sabah',
    author_email='0xl3vi@gmail.com',
    license='MIT',
    keywords=['command line', 'torrent'],
    url='https://github.com/rachmadaniHaryono/we-get',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'docopt',
        'prompt_toolkit>=2.0.3',
        'Pygments>=2.2.0',
    ],
    extras_require={
        'test':  ["pytest", "pytest-flake8", 'vcrpy'], },
    include_package_data=True,
    package_data={'we_get': ['txt/useragents.txt']},
    entry_points={'console_scripts': ['we-get=we_get:main']}
)
