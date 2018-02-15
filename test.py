import unittest
from script import always_true

class TestAlwaysTrue (unittest.TestCase):
    def testAssertNotEqual(self):
        result = always_true()
        self.assertNotEqual(result, False)

if __name__ == "__main__":
    unittest.main()
