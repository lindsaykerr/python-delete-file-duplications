from src.FileCopyDeleter import FileCopyDeleter
from src.config import Config
import unittest
import os, shutil

path, _ = os.path.split(__file__ )
if os.path.isdir(path + "/temp_test_dir"):
    shutil.rmtree(path + "/temp_test_dir")

shutil.copytree("test_dir", "temp_test_dir")
test_dir = "/temp_test_dir"
        
class TestingDeletionList(unittest.TestCase):
    def test_get_files(self):
        deleter = FileCopyDeleter()
        deleter.path = path + "/test_dir/sub_2"
        deleter.types = ["bmp"]    
        self.assertEqual(6, len(deleter.deletion_list))
        deleter.types = ["txt"]
        self.assertEqual(3, len(deleter.deletion_list))
        deleter.types = ["txt", "bmp"]
        self.assertEqual(9, len(deleter.deletion_list))

class TestingFileCopyDeleter(unittest.TestCase):
    def test_set_path(self):
        deleter = FileCopyDeleter()
        deleter.path = "/something"
        deleter.types = ["bmp", "txt"]
        self.assertEqual("/something", deleter.path)
        self.assertEqual(", ".join(["bmp", "txt"]), deleter.types)

    def test_delete_copies(self):
        deleter = FileCopyDeleter()
        deleter.path = path + test_dir + "/"
        deleter.types = ["bmp", "txt"]
        self.assertEqual(11, len(deleter.deletion_list))
        deleter.delete_copies()
        self.assertEqual(0, len(deleter.deletion_list))    


class TestingConfig(unittest.TestCase):
    def test_simple_config(self):
        config = Config(__file__)
        self.assertEqual(config.path, path + "/test_dir/sub_2")
        self.assertEquals(['txt', 'bmp'], config.types)



if __name__ == '__main__':
    unittest.main()