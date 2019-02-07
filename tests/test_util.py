#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from besttags.util import merge, limit, Tags


class TestUtil(unittest.TestCase):

    def test_merge(self):
        t1 = ['a', 'b', 'c', 'd']
        t2 = ['b', 'c', 'e']

        r1 = merge([t1, t2])
        self.assertEqual(r1, {'a': 0.5, 'b': 1, 'c': 1, 'd': 0.5, 'e': 0.5})

        r2 = merge([t1, t2], [1, 1])
        self.assertEqual(r2, {'a': 1, 'b': 2, 'c': 2, 'd': 1, 'e': 1})

    def test_limit(self):
        s1 = {'a': 1, 'b': 2, 'c': 2, 'd': 1, 'e': 1}
        t1 = limit(s1)
        self.assertEqual(len(t1), 5)

        t2 = limit(s1, n=2)
        self.assertEqual(len(t2), 2)

    def test_Tags(self):
        tags = Tags(['a', 'b', 'c', 'd'])
        self.assertEqual(str(tags), '#a #b #c #d')
        self.assertEqual(len(tags), 4)
        self.assertIn('a', tags)
        self.assertNotIn('e', tags)


if __name__ == '__main__':
    unittest.main()
