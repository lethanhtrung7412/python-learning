import sys
import os
import unittest

# Ensure src/ is in PYTHONPATH when running manually
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import hello_world  # now safe to import because of if __name__ == "__main__"

class TestHelloWorld(unittest.TestCase):
    def test_greeting_default(self):
        result = hello_world.greeting("World")
        self.assertEqual(result, "Hello, World!")

    def test_greeting_custom(self):
        result = hello_world.greeting("Alice")
        self.assertEqual(result, "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()
