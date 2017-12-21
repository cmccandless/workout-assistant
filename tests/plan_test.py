import unittest
import plan


class TestPlan(unittest.TestCase):
    def test_exists_add(self):
        self.assertIs(hasattr(plan, 'add'), True)

    def test_exists_list(self):
        self.assertIs(hasattr(plan, 'list'), True)

    def test_exists_details(self):
        self.assertIs(hasattr(plan, 'details'), True)

    def test_exists_stats(self):
        self.assertIs(hasattr(plan, 'stats'), True)

    def test_exists_edit(self):
        self.assertIs(hasattr(plan, 'edit'), True)

    def test_exists_remove(self):
        self.assertIs(hasattr(plan, 'remove'), True)

    def test_exists_run(self):
        self.assertIs(hasattr(plan, 'run'), True)
