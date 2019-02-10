import unittest
from besttags.manager.web import WebManager as Manager


class TestManager(unittest.TestCase):

    def test_init(self):
        self.assertRaises(TypeError, lambda: Manager(kind='atest'))
        self.assertRaises(ValueError, lambda: Manager(limit=1, fix=['a', 'b']))
        self.assertRaises(TypeError, lambda: Manager(fix=2))
        self.assertRaises(TypeError, lambda: Manager(weights=2))

        best1 = Manager(limit=5, fix=['a', 'b'], weights=[1, 3])
        self.assertEqual(best1.limit, 5)
        self.assertEqual(best1.fix, ['a', 'b'])
        self.assertEqual(best1.weights, [1, 3])

        best2 = Manager(fix=['ab'])
        self.assertEqual(best2.fix, ['ab'])

    def test_call(self):
        best = Manager(kind='test', fix=['ab'])
        tags = list(best('test', 'test1'))
        self.assertEqual(len(tags), 3)
        self.assertIn('ab', tags)
        self.assertIn('test', tags)
        self.assertNotIn('e', tags)

        best2 = Manager(kind='test', fix=['a1', 'a2'], limit=4)
        tags2 = list(best2('t1', 't2', 't3'))
        self.assertEqual(len(tags2), 4)


if __name__ == '__main__':
    unittest.main()
