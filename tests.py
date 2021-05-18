from command_line.functions import valid_path
from deletion.functions import get_files  
import unittest
import os

class TestingRemoveDupsFunctions(unittest.TestCase):    

    def test_get_files(self):
        path, _ = os.path.split(__file__ )
        self.assertEqual(6, len(get_files(path + "/test_dir/sub_2", ["bmp"])))
        self.assertEqual(3, len(get_files(path + "/test_dir/sub_2", ["txt"])))
        self.assertEqual(9, len(get_files(path + "/test_dir/sub_2", ["txt", "bmp"])))
        self.assertEqual(11, len(get_files(path)))

    def test_working_path(self):
        path, _ = os.path.split(__file__ )
        self.assertTrue(valid_path(path))
        self.assertTrue(valid_path("test_dir"))
        self.assertFalse(valid_path("Z://test"))
        self.assertTrue(valid_path("C://"))


if __name__ == '__main__':
    unittest.main()