import unittest
import os
from json import load as json_load
from besttags.analyzer.local import DataAnalyzer
from besttags.util.cls import Tags


class TestDataAnalyzer(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'data.json')
        with open(filename, 'r') as f:
            self.data = json_load(f)

    def test_call(self):
        result = DataAnalyzer(data=self.data)('python', 'linux')
        self.assertEqual(len(result), 5)
        self.assertIn('os', result)

    def test_limit(self):
        result = DataAnalyzer(data=self.data, limit=4)('python', 'linux', 'coding')
        self.assertEqual(len(result), 4)
        self.assertIn('python', result)
        self.assertIn('linux', result)
        self.assertIn('coding', result)
        self.assertIn('programming', result)
        self.assertNotIn('software', result)
        self.assertNotIn('programmer', result)
        self.assertNotIn('os', result)

    def test_defaults(self):
        result = DataAnalyzer()('python', 'linux')
        self.assertIsInstance(result, Tags)


if __name__ == '__main__':
    unittest.main()
