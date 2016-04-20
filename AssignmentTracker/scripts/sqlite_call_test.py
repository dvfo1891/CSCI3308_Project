#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import sqlite_call

@classmethod
def tearDownClass(cls):
pass

def setUp(self):
pass

def tearDown(self):
pass

def test_select(self):
sqlite_call.db_insert_user("(112,'root1', 'test1')")
p = sqlite_call.db_select_user(" username = 'root1'")
t = p[0]
sqlite_call.db_delete_user(" username = 'root1'")
self.assertEqual(t[1], "root1", "did not select correctly")

def test_insert(self):
p = sqlite_call.db_select_user(" username = 'root1'")
sqlite_call.db_insert_user("(112,'root1', 'test1')")
t = sqlite_call.db_select_user(" username = 'root1'")
sqlite_call.db_delete_user("username = 'root1'")
self.assertNotEqual(p, t, "did not insert to DB")

def test_Delete(self):
sqlite_call.db_insert_user("(112,'root1', 'test1')")
p = sqlite_call.db_select_user(" username like 'root1'")
sqlite_call.db_delete_user("username = 'root1'")
t = sqlite_call.db_select_user(" username like 'root1'")
self.assertNotEqual(p, t, "did not Delete to DB")

# Add Your Test Cases Here..

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()


