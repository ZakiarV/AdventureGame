import os
from AdventureGameFiles.get_directory_path import get_directory_path


def get_file_list(directory: str = "Saves/") -> list:
    """Gets a list of all the files in a directory.
    :param directory: The directory to get the file list from.
    :return: A list of all the files in the directory.
    """
    directory_path = get_directory_path() + "/" + directory
    file_list = os.listdir(directory_path)
    return file_list
