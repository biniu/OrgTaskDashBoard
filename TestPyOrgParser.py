#!/bin/env python

import unittest

from datetime import datetime

from PyOrgParser import PyOrgParser


class TestPyOrgParser(unittest.TestCase):

    test_class = None
    MOCK_FILE = 'TEST.org'
    TASK_NUMBER = 17

    TASK_ENTRIES = [
        ("** TODO test_task_1"
         "                                            :PRJ_2:TASK_1:"
         "SCHEDULED: <2018-10-17 śro> DEADLINE: <2018-11-21 śro>"
         ":PROPERTIES:"
         ":CREATED:  <2018-10-10 śro 12:32>"
         ":ID:       25b044c9-0e29-42cf-a5e1-fe4ae9cce419"
         ":END:"),
        ("* TODO [#A] TEST_PROJECT_2"
         "                                            :PRJ_2:"
         ":PROPERTIES:"
         ":CREATED:  <2018-10-10 śro 12:31>"
         ":ID:       ef33c4a0-34dd-4ce0-836e-fa35b25be97d"
         ":END:"),
        ("** TODO [#C] test_task_2"
         "DEADLINE: <2018-10-15 pon>"
         ":PROPERTIES:"
         ":CREATED:  <2018-10-10 śro 12:28>"
         ":ID:       a86728d2-ad31-49cd-91bd-88c290677f2a"
         ":END:"),
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
        self.assertEqual(self.test_class.get_task_name(
            self.TASK_ENTRIES[2]), 'test_task_2')


    def test_get_task_priority(self):
        self.assertEqual(self.test_class.get_task_priority(
            self.TASK_ENTRIES[0]), None)
        self.assertEqual(self.test_class.get_task_priority(
            self.TASK_ENTRIES[1]), 'A')
        self.assertEqual(self.test_class.get_task_priority(
            self.TASK_ENTRIES[2]), 'C')

    def test_get_task_deadline(self):
        # 2018-11-21
        test_date_1 = datetime.strptime('2018-11-21', '%Y-%m-%d')
        test_date_2 = datetime.strptime('2018-10-15', '%Y-%m-%d')
        self.assertEqual(self.test_class.get_task_deadline(
            self.TASK_ENTRIES[0]), test_date_1)
        self.assertEqual(self.test_class.get_task_deadline(
            self.TASK_ENTRIES[1]), None)
        self.assertEqual(self.test_class.get_task_deadline(
            self.TASK_ENTRIES[2]), test_date_2)

    def test_get_task_creationdate(self):
        # 2018-10-10 12:32
        test_date_1 = \
            datetime.strptime('2018-10-10 12:32', '%Y-%m-%d %I:%M')
        test_date_2 = \
            datetime.strptime('2018-10-10 12:31', '%Y-%m-%d %I:%M')
        test_date_3 = \
            datetime.strptime('2018-10-10 12:28', '%Y-%m-%d %I:%M')
        self.assertEqual(self.test_class.get_task_creation_date(
            self.TASK_ENTRIES[0]), test_date_1)
        self.assertEqual(self.test_class.get_task_creation_date(
            self.TASK_ENTRIES[1]), test_date_2)
        self.assertEqual(self.test_class.get_task_creation_date(
            self.TASK_ENTRIES[2]), test_date_3)

    def test_get_task_id(self):
        ID_1 = '25b044c9-0e29-42cf-a5e1-fe4ae9cce419'
        ID_2 = 'ef33c4a0-34dd-4ce0-836e-fa35b25be97d'
        ID_3 = 'a86728d2-ad31-49cd-91bd-88c290677f2a'

        self.assertEqual(self.test_class.get_task_id(
            self.TASK_ENTRIES[0]), ID_1)
        self.assertEqual(self.test_class.get_task_id(
            self.TASK_ENTRIES[1]), ID_2)
        self.assertEqual(self.test_class.get_task_id(
            self.TASK_ENTRIES[2]), ID_3)

    def test_get_task_state(self):
        STATE_1 = 'TODO'
        STATE_2 = 'TODO'
        STATE_3 = 'TODO'

        self.assertEqual(self.test_class.get_task_state(
            self.TASK_ENTRIES[0]), STATE_1)
        self.assertEqual(self.test_class.get_task_state(
            self.TASK_ENTRIES[1]), STATE_2)
        self.assertEqual(self.test_class.get_task_state(
            self.TASK_ENTRIES[2]), STATE_3)

    def test_get_task_level(self):
        LEVEL_1 = 2
        LEVEL_2 = 1
        LEVEL_3 = 2

        self.assertEqual(self.test_class.get_task_level(
            self.TASK_ENTRIES[0]), LEVEL_1)
        self.assertEqual(self.test_class.get_task_level(
            self.TASK_ENTRIES[1]), LEVEL_2)
        self.assertEqual(self.test_class.get_task_level(
            self.TASK_ENTRIES[2]), LEVEL_3)

    def test_get_task_tags(self):
        TAGS_1 = ['PRJ_2', 'TASK_1']
        TAGS_2 = ['PRJ_2']
        TAGS_3 = None

        self.assertEqual(self.test_class.get_task_tags(
            self.TASK_ENTRIES[0]), TAGS_1)
        self.assertEqual(self.test_class.get_task_tags(
            self.TASK_ENTRIES[1]), TAGS_2)
        self.assertEqual(self.test_class.get_task_tags(
            self.TASK_ENTRIES[2]), TAGS_3)

    def test_get_struct(self):
        test_date_struct = [
            {'level': 1, 'status': 'TODO', 'priority': 'B',
             'task': 'TEST_PROJECT', 'tags': None, 'deadline': None,
                'created': datetime(2018, 10, 10, 0, 7),
                'id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626',
                'parent_id': 'TEST.org'},
            {'level': 2, 'status': 'TODO', 'priority': 'D',
             'task': 'test_task_1', 'tags': ['PRJ_1', 'TASK_1'],
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 28),
             'id': '17b1ad1a-e5e8-4661-b97a-9740a0c18134',
             'parent_id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626'},
            {'level': 2, 'status': 'TODO', 'priority': 'C',
             'task': 'test_task_2', 'tags': None,
             'deadline': datetime(2018, 10, 15, 0, 0),
             'created': datetime(2018, 10, 10, 0, 28),
             'id': 'a86728d2-ad31-49cd-91bd-88c290677f2a',
             'parent_id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626'},
            {'level': 2, 'status': 'TODO', 'priority': 'A',
             'task': 'test_task_3', 'tags': None,
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 29),
             'id': '0b7079a7-c42f-483b-a647-9f9d543265e5',
             'parent_id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626'},
            {'level': 3, 'status': 'TODO', 'priority': None,
             'task': 'test_sub_task_1', 'tags': None, 'deadline': None,
             'created': datetime(2018, 10, 10, 0, 29),
             'id': 'ae3e2cec-1bf4-453b-8375-d4c4a7e57771',
             'parent_id': '0b7079a7-c42f-483b-a647-9f9d543265e5'},
            {'level': 3, 'status': 'TODO', 'priority': 'A',
             'task': 'test_sub_task_2a', 'tags': None,
             'deadline': datetime(2018, 10, 19, 0, 0),
             'created': datetime(2018, 10, 10, 0, 29),
             'id': '54466717-f316-43e2-b4a1-70d5539d6d83',
             'parent_id': '0b7079a7-c42f-483b-a647-9f9d543265e5'},
            {'level': 4, 'status': 'TODO', 'priority': 'A',
             'task': 'test_Sub_task_1', 'tags': None,
             'deadline': datetime(2018, 10, 16, 0, 0),
             'created': datetime(2018, 10, 10, 0, 29),
             'id': 'ea15f614-7240-4bcb-801d-cb24e8093a69',
             'parent_id': '54466717-f316-43e2-b4a1-70d5539d6d83'},
            {'level': 5, 'status': 'TODO', 'priority': None,
             'task': 'test_sub_sub_sub_task_1', 'tags': None,
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 30),
             'id': '05716185-b29d-4bad-b832-8a48a092faf0',
             'parent_id': 'ea15f614-7240-4bcb-801d-cb24e8093a69'},
            {'level': 5, 'status': 'TODO', 'priority': None,
             'task': 'test_sub_sub_sub_task_2', 'tags': None,
             'deadline': None, 'created': datetime(
                 2018, 10, 10, 0, 30),
             'id': '5e78562b-2bb2-44a6-9f51-fd68bd47e25c',
             'parent_id': 'ea15f614-7240-4bcb-801d-cb24e8093a69'},
            {'level': 4, 'status': 'TODO', 'priority': 'D',
             'task': 'test_sub_sub_task_2', 'tags': None,
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 30),
             'id': '90fde36d-393a-436c-b3d8-4a46af0014c9',
             'parent_id': '54466717-f316-43e2-b4a1-70d5539d6d83'},
            {'level': 4, 'status': 'DONE', 'priority': 'B',
             'task': 'test_sub_sub_task_3', 'tags': None,
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 30),
             'id': '4cbe2571-a64e-4708-b482-b4d864938960',
             'parent_id': '54466717-f316-43e2-b4a1-70d5539d6d83'},
            {'level': 3, 'status': 'TODO', 'priority': None,
             'task': 'test_sub_task_3', 'tags': None,
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 31),
             'id': '5f431613-941a-4872-9232-f85379ee8fda',
             'parent_id': '0b7079a7-c42f-483b-a647-9f9d543265e5'},
            {'level': 2, 'status': 'TODO', 'priority': 'A',
             'task': 'test_task_4', 'tags': None,
             'deadline': None,
                'created': None,
                'id': '3e022bfd-7c92-4911-8ec7-54c81474e065',
                'parent_id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626'},
            {'level': 2, 'status': 'TODO', 'priority': None,
             'task': 'test_task_5', 'tags': None,
             'deadline': None,
                'created': None,
                'id': '6a11fd79-40ca-4fc8-a0c3-eeec5085ba6e',
                'parent_id': '9fffbef3-173b-4de2-b7ab-a53e0bf48626'},
            {'level': 1, 'status': 'TODO', 'priority': 'A',
             'task': 'TEST_PROJECT_2', 'tags': ['PRJ_2'],
             'deadline': None,
             'created': datetime(2018, 10, 10, 0, 31),
             'id': 'ef33c4a0-34dd-4ce0-836e-fa35b25be97d',
             'parent_id': 'TEST.org'},
            {'level': 2, 'status': 'TODO', 'priority': None,
             'task': 'test_task_1', 'tags': ['PRJ_2', 'TASK_1'],
             'deadline': datetime(2018, 11, 21, 0, 0),
             'created': datetime(2018, 10, 10, 0, 32),
             'id': '25b044c9-0e29-42cf-a5e1-fe4ae9cce419',
             'parent_id': 'ef33c4a0-34dd-4ce0-836e-fa35b25be97d'},
            {'level': 2, 'status': 'TODO', 'priority': None,
             'task': 'test_task_2', 'tags': None,
             'deadline': datetime(2018, 11, 22, 0, 0),
             'created': datetime(2018, 10, 10, 0, 32),
             'id': '3ee03e4c-c42f-48dc-a16c-f55228eec9b0',
             'parent_id': 'ef33c4a0-34dd-4ce0-836e-fa35b25be97d'},
        ]

        self.assertEqual(test_date_struct, self.test_class.get_struct())
