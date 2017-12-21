import unittest
import buddy


class TestBuddy(unittest.TestCase):
    def test_exists_add(self):
        self.assertIs(hasattr(buddy, 'add'), True)

    def test_exists_list(self):
        self.assertIs(hasattr(buddy, 'list'), True)

    def test_exists_stats(self):
        self.assertIs(hasattr(buddy, 'stats'), True)

    def test_exists_remove(self):
        self.assertIs(hasattr(buddy, 'remove'), True)
