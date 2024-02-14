import os


def get_directory_path():
    """Gets the path of the directory containing the game files.
    :return: The path of the directory containing the game files.
    """
    directory_path = os.path.dirname(os.path.abspath(__file__))
    return directory_path