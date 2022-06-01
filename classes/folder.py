from array import array
from option import Option
import os


class Folder:

    __options = list

    def __init__(self, folder_path: str):
        self.__folder_path = folder_path

    def add_option(self, destination_path: str, extensions: array):
        self.__options.append(Option(destination_path, extensions))

    def start_cleaning(self):
        files = os.listdir(self.__folder_path)
        for file in files:
            for option in self.__options:
                if option.__contains(file):
                    option.__move_file(self.__folder_path, file)
