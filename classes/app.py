from genericpath import exists
from folder import Folder


class App:

    __folders = list

    def run(self):
        if (exists(self.Folders)):
            for folder in self.folders:
                folder.start_cleaning

    def add_folder(self, folder_path: str):
        self.__folders.append(Folder(folder_path))
