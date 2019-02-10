import unittest
import os
from json import load as json_load
from besttags.analyzer.local import DBAnalyzer
from besttags.util.cls import Tags


class TestDBAnalyzer(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'data.json')
        with open(filename, 'r') as f:
            data = json_load(f)

        self.analyzer = DBAnalyzer('test.db', limit=4)
        self.analyzer.manager.setup()
        for tag, related in data.items():
            self.analyzer.manager.add(tag, related)

    def tearDown(self):
        self.analyzer.manager.delete()

    def test_limit(self):
        result = self.analyzer('python', 'linux', 'coding')
        self.assertEqual(len(result), 4)
        self.assertIn('python', result)
        self.assertIn('linux', result)
        self.assertIn('coding', result)
        self.assertIn('programming', result)
        self.assertNotIn('software', result)
        self.assertNotIn('programmer', result)
        self.assertNotIn('os', result)


if __name__ == '__main__':
    unittest.main()
