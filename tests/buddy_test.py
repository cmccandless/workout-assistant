import unittest
import buddy
from tinydb import TinyDB


class TestBuddy(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test.db.json'
        self.db = TinyDB(self.db_path)
        self.db.purge()

    def tearDown(self):
        self.db.purge()

    def test_exists_add(self):
        self.assertIs(hasattr(buddy, 'add'), True)

    def test_exists_ls(self):
        self.assertIs(hasattr(buddy, 'ls'), True)

    def test_exists_log(self):
        self.assertIs(hasattr(buddy, 'log'), True)

    def test_exists_stats(self):
        self.assertIs(hasattr(buddy, 'stats'), True)

    def test_exists_remove(self):
        self.assertIs(hasattr(buddy, 'remove'), True)
