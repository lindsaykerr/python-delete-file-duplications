from deletion.functions import get_deletion_list 
from deletion.FileCopyDeleter import FileCopyDeleter
import unittest
import os


class TestingFileRetrieval(unittest.TestCase):
    def test_get_files(self):
        path, _ = os.path.split(__file__ )
        self.assertEqual(6, len(get_deletion_list(path + "/test_dir/sub_2", ["bmp"])))
        self.assertEqual(3, len(get_deletion_list(path + "/test_dir/sub_2", ["txt"])))
        self.assertEqual(9, len(get_deletion_list(path + "/test_dir/sub_2", ["txt", "bmp"])))
 


class TestingDeletionList(unittest.TestCase):
    def test_get_files(self):
        path, _ = os.path.split(__file__ )
        deleter = FileCopyDeleter()
        deleter.path = path + "/test_dir/sub_2"
        deleter.types = ["bmp"]    
        self.assertEqual(6, len(deleter.deletion_list))
        deleter.types = ["txt"]
        self.assertEqual(3, len(deleter.deletion_list))
        deleter.types = ["txt", "bmp"]
        self.assertEqual(9, len(deleter.deletion_list))

class TesstingFileCopyDeleterObject(unittest.TestCase):
    def test_set_path(self):
        deleter = FileCopyDeleter()
        deleter.path = "/something"
        deleter.types = ["bmp", "txt"]
        self.assertEquals("/something", deleter.path)
        self.assertEquals(", ".join(["bmp", "txt"]), deleter.types)


if __name__ == '__main__':
    unittest.main()