import shutil
import pathlib
import os

class FileMover:
    def __init__(self, path):
        self.path = path

    def get_files(self):
        files = []
        store = os.listdir(self.path)
        for file in store:
            files.append(file)
            
        return files
        
    def assign_folders(self, files):
        from_folder = self.path
        to_folder = 'C:\\Users\\smushwan\\Desktop\\two'
        
        if pathlib.Path(from_folder).exists() and pathlib.Path(to_folder).exists():
            for i in files:
                filename, extension = os.path.splitext(i)
                if extension == '.exe':
                    shutil.move(from_folder+'\\'+i, to_folder+'\\a\\'+i)
                if extension == '.pdf':
                    shutil.move(from_folder+'\\'+i, to_folder+'\\b\\'+i)
                if extension == '.rar':
                    shutil.move(from_folder+'\\'+i, to_folder+'\\c\\'+i)


    def move_files(self):
        try:
           files = self.get_files()
           self.assign_folders(files)
           print('Files moved')
        except NameError:
            print('There was a problem moving the file')


move = FileMover('C:\\Users\\smushwan\\Desktop\\one')
move.move_files()
