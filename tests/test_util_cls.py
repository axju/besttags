import unittest

from besttags.util.cls import Tags


class TestUtil(unittest.TestCase):

    def test_Tags(self):
        tags = Tags(['a', 'b', 'c', 'd'])
        self.assertEqual(str(tags), '#a #b #c #d')
        self.assertEqual(len(tags), 4)
        self.assertIn('a', tags)
        self.assertNotIn('e', tags)


if __name__ == '__main__':
    unittest.main()
