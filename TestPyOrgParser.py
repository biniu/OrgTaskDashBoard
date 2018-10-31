#!/bin/env python

import unittest

import PyOrgParser

class TestPyOrgParser(unittest.TestCase):

    test_class = None
    MOCK_FILE = 'TEST.org'

    def setUp(self):
        print("setUp")
        self.test_class = PyOrgParser(self.MOCK_FILE)

    def tearDown(self):
        print("tearDown")
        del self.test_class
