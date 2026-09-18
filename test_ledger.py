import unittest
import os
import csv
from ledger import record_transaction

class TestLedger(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_deals.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_record_transaction(self):
        record_transaction("Client A", "Scriptwriting", 150.0, filename=self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
        
        with open(self.test_file, mode="r") as f:
            reader = list(csv.reader(f))
            self.assertEqual(len(reader), 2)  # Header + 1 entry
            self.assertEqual(reader[1][0], "Client A")

if __name__ == "__main__":
    unittest.main()
