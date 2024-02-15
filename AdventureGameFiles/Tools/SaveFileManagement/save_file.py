import pyexcel as pe
from typing import Union


def save_data(data: Union[list, dict], file_name: str, directory: str = "Saves/") -> None:
    """Saves data to a file.
    :param data: The data to save.
    :param file_name: The name of the file to save to.
    :param directory: The directory to save the file to.
    """
    full_path = directory + file_name
    sheet = pe.Sheet(data)
    sheet.save_as(full_path)
