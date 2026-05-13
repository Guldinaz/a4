import os
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    def check_file(self):
        return os.path.exists(self.file_path)
    def create_output_folder(self):
        if not os.path.exists('output'):
            os.makedirs('output')
