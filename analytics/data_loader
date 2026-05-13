import csv
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students =[]
    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.students = list(csv.DictReader(f))
