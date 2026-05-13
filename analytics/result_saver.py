import json
class ResultSaver:
    def __init__(self, result_data, file_path):
        self.result_data = result_data
        self.file_path = file_path
    def save_json(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.result_data, f, indent=4)
