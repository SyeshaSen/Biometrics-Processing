import unittest

import sys
import os

sys.path.append(".")
from src.fingerprint import Fingerprint
from src.login import Login, MaxTriesExceededError

class Test_Login(unittest.TestCase):
    
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    original = Fingerprint.from_file(os.path.join(data_dir, "Original.txt"))
    other_user = Fingerprint.from_file(os.path.join(data_dir, "User1.txt"))
    variation = Fingerprint.from_file(os.path.join(data_dir, "variation1.txt"))

    def test_happy_case(self) -> None:
        """Tests happy case, when the fingerpring authentication is valid"""
        login = Login(self.original, max_tries=3)
        self.assertTrue(login.authenticate(self.variation, match_threshold=0.8))

    def test_negative_case(self) -> None:
        """Tests incorrect fingerprint authentication."""
        login = Login(self.original, max_tries=3)
        result = login.authenticate(self.other_user)
        self.assertFalse(result)

    def test_edge_case_max_tries(self) -> None:
        """Test edge case where max attempts have been reached"""
        login = Login(self.original, max_tries=2)
        login.authenticate(self.other_user)
        with self.assertRaises(MaxTriesExceededError):
            login.authenticate(self.other_user)

    if __name__ == "__main__":
        unittest.main()