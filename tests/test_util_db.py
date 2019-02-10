import unittest

from besttags.util.db import Manager


class BasicTestUtilDB(unittest.TestCase):

    def setUp(self):
        self.manager = Manager('test.db')
        self.manager.setup()

    def tearDown(self):
        self.manager.delete()


class TestUtilDB(BasicTestUtilDB):

    def test_add_str(self):
        self.manager.add('test1', 'a')
        tags = self.manager.get('test1')
        self.assertIn('a', tags)

    def test_add_list(self):
        self.manager.add('test2', ['a', 'b', 'c'])
        tags = self.manager.get('test2')
        self.assertIn('a', tags)
        self.assertIn('b', tags)
        self.assertIn('c', tags)

    def test_add_dict(self):
        self.manager.add('test3', {'a': 0.2, 'b': 0.8, 'c': 0.5})
        tags = self.manager.get('test3')
        self.assertIn('a', tags)
        self.assertIn('b', tags)
        self.assertIn('c', tags)

    def test_add_dict(self):
        self.manager.add('test2', ['a', 'b', 'c'])
        n = len(self.manager.all())

        self.manager.add('test2', ['a', 'b', 'c'])
        self.assertEqual(len(self.manager.all()), n)


if __name__ == '__main__':
    unittest.main()
