import pyexcel as pe


def load_data(file_name: str, directory: str = "Saves/") -> list:
    """Loads data from a file and returns it as a list.
    :param file_name: The name of the file to load.
    :param directory: The directory to load the file from.
    :return: A list of the data from the file.
    """
    full_path = directory + file_name
    file = pe.get_sheet(file_path=full_path)
    data = file.to_array()
    return data
