#!/bin/env python

import unittest

from datetime import datetime

from PyOrgParser import PyOrgParser


class TestPyOrgParser(unittest.TestCase):

    test_class = None
    MOCK_FILE = 'TEST.org'
    TASK_NUMBER = 17

    TASK_ENTRIES = [
        ("** TODO test_task_1   SCHEDULED: <2018-10-17 śro>"
         " DEADLINE: <2018-11-21 śro>   :PROPERTIES:   :CREATED:"
         "  <2018-10-10 śro 12:32>   "
         ":ID:       25b044c9-0e29-42cf-a5e1-fe4ae9cce419   :END:"),
        ("* TODO [#A] TEST_PROJECT_2"
         ":PROPERTIES:"
         ":CREATED:  <2018-10-10 śro 12:31>"
         ":ID:       ef33c4a0-34dd-4ce0-836e-fa35b25be97d"
         ":END:"
         ),
    ]

    def setUp(self):
        self.test_class = PyOrgParser(self.MOCK_FILE)

    def tearDown(self):
        del self.test_class

    def test_get_task_number(self):
        self.assertEqual(self.test_class.get_task_number(),
                         self.TASK_NUMBER)

    def test_get_task_name(self):
        self.assertEqual(self.test_class.get_task_name(
            self.TASK_ENTRIES[0]), 'test_task_1')
        self.assertEqual(self.test_class.get_task_name(
            self.TASK_ENTRIES[1]), 'TEST_PROJECT_2')

    def test_get_task_priority(self):
        self.assertEqual(self.test_class.get_task_priority(
            self.TASK_ENTRIES[0]), None)
        self.assertEqual(self.test_class.get_task_priority(
            self.TASK_ENTRIES[1]), 'A')

    def test_get_task_deadline(self):
        # 2018-11-21
        test_date = datetime.strptime('2018-11-21', '%Y-%m-%d')
        self.assertEqual(self.test_class.get_task_deadline(
            self.TASK_ENTRIES[0]), test_date)
        self.assertEqual(self.test_class.get_task_deadline(
            self.TASK_ENTRIES[1]), None)

    def test_get_task_creationdate(self):
        # 2018-10-10 12:32
        test_date_1 = \
            datetime.strptime('2018-10-10 12:32', '%Y-%m-%d %I:%M')
        test_date_2 = \
            datetime.strptime('2018-10-10 12:31', '%Y-%m-%d %I:%M')
        self.assertEqual(self.test_class.get_task_creation_date(
            self.TASK_ENTRIES[0]), test_date_1)
        self.assertEqual(self.test_class.get_task_creation_date(
            self.TASK_ENTRIES[1]), test_date_2)

    def test_get_task_id(self):
        ID_1 = '25b044c9-0e29-42cf-a5e1-fe4ae9cce419'
        ID_2 = 'ef33c4a0-34dd-4ce0-836e-fa35b25be97d'

        self.assertEqual(self.test_class.get_task_id(
            self.TASK_ENTRIES[0]), ID_1)
        self.assertEqual(self.test_class.get_task_id(
            self.TASK_ENTRIES[1]), ID_2)

    def test_get_task_state(self):
        STATE_1 = 'TODO'
        STATE_2 = 'TODO'

        self.assertEqual(self.test_class.get_task_state(
            self.TASK_ENTRIES[0]), STATE_1)
        self.assertEqual(self.test_class.get_task_state(
            self.TASK_ENTRIES[1]), STATE_2)

    def test_get_task_state(self):
        LEVEL_1 = 2
        LEVEL_2 = 1

        self.assertEqual(self.test_class.get_task_level(
            self.TASK_ENTRIES[0]), LEVEL_1)
        self.assertEqual(self.test_class.get_task_level(
            self.TASK_ENTRIES[1]), LEVEL_2)
