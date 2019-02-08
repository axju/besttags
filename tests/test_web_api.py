#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from besttags.web.apis import best_hashtags


class TestApis(unittest.TestCase):

    def test_best_hashtags(self):
        t1 = best_hashtags('coding')
        self.assertEqual(len(t1), 30)

        t2 = best_hashtags('coding', kind='liked')
        self.assertEqual(len(t2), 30)

        t3 = best_hashtags('cfgsf345treswe345zhrtgfdew3r45556')
        self.assertFalse(t3)


if __name__ == '__main__':
    unittest.main()
