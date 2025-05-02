
import unittest
import os
from file_handler import save_result, load_results

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "results.csv"
        # Ištrinam, jei buvo
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_result(self):
        save_result("A", "B", "A laimėjo")
        results = load_results()
        self.assertIn(["A", "B", "A laimėjo"], results)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
