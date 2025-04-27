import unittest
import sys
import os

# Add the root directory to the Python path to find the user_authentication module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user_authentication import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        """Tests that login returns True for valid (non-empty) credentials."""
        self.assertTrue(login("testuser", "password123"))

    def test_empty_username(self):
        """Tests that login raises ValueError for an empty username."""
        with self.assertRaises(ValueError) as context:
            login("", "password123")
        self.assertEqual(str(context.exception), "Username and password cannot be empty.")

    def test_empty_password(self):
        """Tests that login raises ValueError for an empty password."""
        with self.assertRaises(ValueError) as context:
            login("testuser", "")
        self.assertEqual(str(context.exception), "Username and password cannot be empty.")

if __name__ == '__main__':
    unittest.main()
