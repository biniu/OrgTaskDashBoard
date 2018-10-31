#!/bin/env python

import unittest

from PyOrgParser import PyOrgParser


class TestPyOrgParser(unittest.TestCase):

    test_class = None
    MOCK_FILE = 'TEST.org'
    TASK_NUMBER = 17

    def setUp(self):
        self.test_class = PyOrgParser(self.MOCK_FILE)

    def tearDown(self):
        del self.test_class

    def test_get_task_number(self):
        self.assertEqual(self.test_class.get_task_number(),
                         self.TASK_NUMBER)
