from analytics
import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser
import TopStudentsAnalyser
if __name__ == "__main__":
    file_name = 'students.csv'
    fm = FileManager(file_name)
    if fm.check_file():
        fm.create_output_folder()
        dl = DataLoader(file_name)
        dl.load()
        analyser = TopStudentsAnalyser(dl.students)
        saver = ResultSaver(analyser.result, 'output/result.json')
        report = Report(analyser, saver)
        report.generate()
