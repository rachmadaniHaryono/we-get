#!/usr/bin/env python
"""test_arguments.py - test the command line arguments
"""

import docopt
from we_get.core.we_get import __doc__
import unittest
import sys


class TestsArguments(unittest.TestCase):
    def test_number_of_arguments(self):
        args = docopt.docopt(__doc__)
        self.assertEqual(len(args), 14)

    def test_required_argument_search(self):
        sys.argv = ['prog_name', '--search']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_target(self):
        sys.argv = ['prog_name', '--target']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_filter(self):
        sys.argv = ['prog_name', '--filter']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_results(self):
        sys.argv = ['prog_name', '--results']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_quality(self):
        sys.argv = ['prog_name', '--quality']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_genre(self):
        sys.argv = ['prog_name', '--genre']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_required_argument_sort_type(self):
        sys.argv = ['prog_name', '--sort-type']
        self.assertRaises(docopt.DocoptExit, docopt.docopt, __doc__)

    def test_no_required_argument_list(self):
        sys.argv = ['prog_name', '--list']
        try:
            docopt.docopt(__doc__)
        except docopt.DocoptExit:
            self.fail('--list required argument!')

    def test_no_required_argument_links(self):
        sys.argv = ['prog_name', '--links']
        try:
            docopt.docopt(__doc__)
        except docopt.DocoptExit:
            self.fail('--links required argument!')

    def test_no_required_argument_get_list(self):
        sys.argv = ['prog_name', '--get-list']
        try:
            docopt.docopt(__doc__)
        except docopt.DocoptExit:
            self.fail('--get-list required argument!')

    def test_no_required_argument_version(self):
        sys.argv = ['prog_name', '--version']
        try:
            docopt.docopt(__doc__)
        except docopt.DocoptExit:
            self.fail('--version required argument!')

    def test_no_required_argument_json(self):
        sys.argv = ['prog_name', '--json']
        try:
            docopt.docopt(__doc__)
        except docopt.DocoptExit:
            self.fail('--json required argument!')


if __name__ == '__main__':
    unittest.main()
