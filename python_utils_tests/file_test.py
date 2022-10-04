import os
import unittest
import warnings
from python_utils.file import *


class TestFileUtil(unittest.TestCase):
    def test_ensure_dir(self):
        # make sure, the directory is created and removed properly
        test_folder = r"testdata\\testdir"
        ensure_dir_created(test_folder)
        self.assertTrue(os.path.exists(test_folder))
        ensure_dir_removed(test_folder)
        self.assertFalse(os.path.exists(test_folder))

        # remove data finally
        ensure_dir_removed("testdata")

    def test_dict_json(self):
        # make sure, a dict os saved as json and read back correctly
        json_file = r"testdata\\testfile.json"
        data = {"a": "xyz", "b": 123, "c": 12.3}
        save_dict_to_json(data, json_file)
        self.assertTrue(os.path.exists(json_file))
        data_read = load_json_to_dict(json_file)
        self.assertDictEqual(data, data_read)

        # remove data finally
        ensure_dir_removed("testdata")

    def test_list_find_file_and_clear_dir(self):
        # save some files
        test_files = [f"testdata\\testdir1\\testfile{k}.json" for k in range(3)]
        for test_file in test_files:
            save_dict_to_json({"abc": 123}, test_file)
        # make sure all saved files are listed
        files = list_files("testdata\\testdir1", suffix=".json")
        self.assertListEqual(files, test_files)
        # make sure an exception is raised if no file is found
        self.assertRaises(
            FileNotFoundError,
            find_file,
            directory="testdata",
            file_name="testfile100.json",
        )
        # make sure a warning is logged if file is not unique
        save_dict_to_json({"abc": 123}, "testdata\\testdir2\\testfile0.json")
        with self.assertLogs(level=logging.WARN):
            find_file(
                directory="testdata",
                file_name="testfile0.json",
            )

        file = find_file(
            directory="testdata",
            file_name="testfile1.json",
        )
        self.assertEqual(file, "testdata\\testdir1\\testfile1.json")

        # remove data finally
        ensure_dir_removed("testdata")
