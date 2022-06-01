import os
from array import array


class Option:

    def __init__(self, destination_path: str, etensions: array):
        self.__destination_path = destination_path
        self.__extensions = etensions

    def conatins(self, file_name: str) -> bool:
        found = False
        for extension in self.__extensions:
            if extension in file_name:
                found = True
                break
        return found

    def move_file(self, folder_path: str, file_name: str):
        file_full_path = folder_path + file_name
        file_destination_full_path = self.__destination_path + file_name
        os.replace(file_full_path, file_destination_full_path)
