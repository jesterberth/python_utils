import os
import shutil
import json
import errno
import logging
from typing import List


def ensure_dir_created(directory) -> None:
    """
    Creates a directory if not existing and logs a feedback.

    Parameters
    ----------
    directory : string
        Absolute directory string.
    Returns
    -------
    None.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info("Directory " + str(directory) + " created")


def ensure_dir_removed(directory) -> None:
    """
    Removes a directory if existing and logs a feedback.

    Parameters
    ----------
    directory : string
        Absolute directory string.
    Returns
    -------
    None.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)
        logging.info("Directory " + str(directory) + " removed")


def clear_dir_content(directory) -> None:
    """
    Clears a directory's content and logs a feedback

    Parameters
    ----------
    directory : string
        Absolute directory string.

    Returns
    -------
    None.

    """
    if os.path.isdir(directory):
        # remove recursively
        shutil.rmtree(directory)
        # recreate the folder
        os.makedirs(directory)
        logging.info("Directory " + str(directory) + " cleared")


def list_files(directory, suffix=".zip") -> List[str]:
    """
    Lists all files with a given suffix in a directory and sub-directories

    Parameters
    ----------
    directory : path, string
        directory with files to list.
    suffix : string, optional
        filter suffix. The default is '.zip'.

    Returns
    -------
    files_list : list of strings
        File names of all matching files in the directory.

    """

    files_list = []
    for subdir, dirs, files in os.walk(directory):
        for filename in sorted(files):
            filepath = os.path.join(subdir, filename)
            if filepath.endswith(suffix):
                files_list.append(filepath)
    logging.info(
        "found " + str(len(files_list)) + " " + suffix + " files in " + directory
    )
    return files_list


def find_file(directory, file_name) -> str:
    """
    Find a file in a directory and sub-directories and return the absolute path

    Parameters
    ----------
    directory : path, string
        directory to search.
    file_name : string
        file name to search for

    Raises
    ------
    FileNotFoundError
        if file not found in directory or sub-directories

    Returns
    -------
    file : str
        matching file

    """

    all_files = list_files(directory, file_name)

    if len(all_files) == 0:
        logging.error("no file named " + file_name + " found in " + directory)
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_name)
    if len(all_files) > 1:
        logging.warn("more than one file named " + file_name + " found in " + directory)
    return all_files[0]


def save_dict_to_json(data: dict, save_path) -> None:
    """
    saves a dictionary to a json file on disk

    Parameters
    ----------
    data : dict
        data dictionary to save.
    save_path : path/string
        absolute sink path.

    Returns
    -------
    None.

    """
    ensure_dir_created(os.path.dirname(save_path))
    with open(save_path, "w") as fp:
        json.dump(data, fp)
    logging.info("Dictionary saved to " + str(save_path))


def load_json_to_dict(load_path) -> dict:
    """
    loads a dictionary from a json file from disk

    Parameters
    ----------
    load_path : path/string
        absolute source path.

    Returns
    -------
    dict
        json file data as dictionary.

    """

    with open(load_path) as fp:
        data = json.load(fp)
    logging.info("Dictionary read from " + str(load_path))
    return data
