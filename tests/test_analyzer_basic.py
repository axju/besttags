#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from besttags.analyzer.basic import BasicAnalyzer as Analyzer
from besttags.util.cls import Tags


class TestBasicAnalyzer(unittest.TestCase):

    def test_except(self):
        self.assertRaises(ValueError, lambda: Analyzer(limit=1, fix=['a', 'b']))
        self.assertRaises(TypeError, lambda: Analyzer(fix=2))

    def test_init_fix_list(self):
        best = Analyzer(limit=5, fix=['a', 'b'])
        self.assertEqual(best.limit, 5)
        self.assertEqual(best.fix, ['a', 'b'])

    def test_init_fix_str(self):
        best = Analyzer(fix='ab')
        self.assertEqual(best.fix, ['ab'])

    def test_call(self):
        best = Analyzer()
        best('a', 'b', 'c')
        self.assertEqual(best.tags, ['a', 'b', 'c'])
        best(['d', 'e', 'f'])
        self.assertEqual(best.tags, ['d', 'e', 'f'])

    def test_get_tags(self):
        best = Analyzer()
        t = best.get_tags(['a', 'b', 'c'])
        self.assertIsInstance(t, Tags)
        self.assertEqual(len(t), 3)
        self.assertEqual(list(t), ['a', 'b', 'c'])

    def test_get_tags_fix(self):
        best = Analyzer(fix='g')
        t = best.get_tags(['a', 'b', 'c'])
        self.assertEqual(len(t), 4)
        self.assertEqual(list(t), ['g', 'a', 'b', 'c'])

    def test_get_tags_limit(self):
        best = Analyzer(fix='g', limit=3)
        t = best.get_tags(['a', 'b', 'c'])
        self.assertEqual(len(t), 3)
        self.assertEqual(list(t), ['g', 'a', 'b'])

if __name__ == '__main__':
    unittest.main()
