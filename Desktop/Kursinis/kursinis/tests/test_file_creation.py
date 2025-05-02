
import unittest
import os
from file_handler import save_result

class TestFileHandlerCreate(unittest.TestCase):
    def test_file_created_if_missing(self):
        test_path = "results.csv"
        if os.path.exists(test_path):
            os.remove(test_path)
        save_result("Test1", "Test2", "Test1 laimėjo")
        self.assertTrue(os.path.exists(test_path))
        os.remove(test_path)

if __name__ == "__main__":
    unittest.main()
