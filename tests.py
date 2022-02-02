from command_line.functions import valid_path
from deletion.functions import get_deletion_list  
import unittest
import os

class TestingFileRetrieval(unittest.TestCase):
    def test_get_files(self):
        path, _ = os.path.split(__file__ )
        self.assertEqual(6, len(get_deletion_list(path + "/test_dir/sub_2", ["bmp"])))
        self.assertEqual(3, len(get_deletion_list(path + "/test_dir/sub_2", ["txt"])))
        self.assertEqual(9, len(get_deletion_list(path + "/test_dir/sub_2", ["txt", "bmp"])))
 



if __name__ == '__main__':
    unittest.main()