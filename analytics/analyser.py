class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self): print("Not implemented")
    def print_results(self):
        for k, v in self.result.items(): print(f"{k}: {v}")
    def __str__(self): return f"DataAnalyser: {len(self.students)} students"

class TopStudentsAnalyser(DataAnalyser):
    def analyse(self):
        top = list(filter(lambda s: float(s['GPA']) == 4.0, self.students))
        self.result = {'total_students': len(self.students), 'high_performers': len(top)}
    def print_results(self):
        print("-" * 30 + "\nTOP STUDENTS ANALYSIS REPORT\n" + "-" * 30)
        super().print_results()
        print("-" * 30)
