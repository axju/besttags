import unittest
import os
from besttags.analyzer.local import FileAnalyzer
from besttags.util.cls import Tags


filename = os.path.join(os.path.dirname(__file__), 'data.json')


class TestFileAnalyzer(unittest.TestCase):

    def test_call(self):
        result = FileAnalyzer(filename=filename)('python', 'linux')
        self.assertEqual(len(result), 5)
        self.assertIn('os', result)

    def test_limit(self):
        result = FileAnalyzer(filename=filename, limit=4)('python', 'linux', 'coding')
        self.assertEqual(len(result), 4)
        self.assertIn('python', result)
        self.assertIn('linux', result)
        self.assertIn('coding', result)
        self.assertIn('programming', result)
        self.assertNotIn('software', result)
        self.assertNotIn('programmer', result)
        self.assertNotIn('os', result)

    def test_defaults(self):
        result = FileAnalyzer()('python', 'linux')
        self.assertIsInstance(result, Tags)




if __name__ == '__main__':
    unittest.main()
