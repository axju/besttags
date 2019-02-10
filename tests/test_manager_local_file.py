import unittest
import os
from besttags.manager.local import FileManager
from besttags.util.cls import Tags


filename = os.path.join(os.path.dirname(__file__), 'test_data.json')


class TestFileManager(unittest.TestCase):

    def test_call(self):
        result = FileManager(filename=filename)('python', 'linux')
        self.assertEqual(len(result), 5)
        self.assertIn('os', result)

    def test_limit(self):
        result = FileManager(filename=filename, limit=4)('python', 'linux', 'coding')
        self.assertEqual(len(result), 4)
        self.assertIn('python', result)
        self.assertIn('linux', result)
        self.assertIn('coding', result)
        self.assertIn('programming', result)
        self.assertNotIn('software', result)
        self.assertNotIn('programmer', result)
        self.assertNotIn('os', result)

    def test_defaults(self):
        result = FileManager()('python', 'linux')
        self.assertIsInstance(result, Tags)




if __name__ == '__main__':
    unittest.main()
