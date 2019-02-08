import unittest
from besttags.local.manager import DataManager
from besttags.util import Tags


data = {
    "coding": {
        "programming": 0.9,
        "software": 0.6,
        "linux": 0.4
    },
    "linux": {
        "coding": 1,
        "os": 0.5
    },
    "python": {
        "coding": 0.8,
        "programmer": 0.6
    }
}


class TestDataManager(unittest.TestCase):

    def test_call(self):
        result = DataManager(data=data)('python', 'linux')
        self.assertEqual(len(result), 5)
        self.assertIn('os', result)

    def test_limit(self):
        result = DataManager(data=data, limit=4)('python', 'linux', 'coding')
        self.assertEqual(len(result), 4)
        self.assertIn('python', result)
        self.assertIn('linux', result)
        self.assertIn('coding', result)
        self.assertIn('programming', result)
        self.assertNotIn('software', result)
        self.assertNotIn('programmer', result)
        self.assertNotIn('os', result)

    def test_defaults(self):
        result = DataManager()('python', 'linux')
        self.assertIsInstance(result, Tags)


if __name__ == '__main__':
    unittest.main()
