import unittest
import sys
import os

sys.path.append(".")
from src.fingerprint import Fingerprint

class TestFingerprint(unittest.TestCase):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    original = Fingerprint.from_file(os.path.join(data_dir, "Original.txt"))
    user1 = Fingerprint.from_file(os.path.join(data_dir, "User1.txt"))
    variation1 = Fingerprint.from_file(os.path.join(data_dir, "variation1.txt"))

    def test_happy_case(self) -> None:
        """Tests a happy case for the fingerprint comparison, where the original matches a variation"""
        Fingerprint.match_threshold = 0.9
        self.assertTrue(self.original == self.variation1)

    def test_negative_case(self) -> None:
        """Tests the negative case, where the original should not match another user that is completely different"""
        Fingerprint.match_threshold = 0.9
        self.assertFalse(self.original == self.user1)

    def test_edge_case(self) -> None:
        """Tests the edge case where if the threshold is a bit higher, the variation and the original do not match"""
        Fingerprint.match_threshold = 0.97
        self.assertFalse(self.original == self.variation1)

    if __name__ == "__main__":
        unittest.main()
