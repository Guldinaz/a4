#test_analyse_twice (tests.test_analyser.TestAnalyser.test_analyse_twice) ... ok
#test_result_has_required_keys (tests.test_analyser.TestAnalyser.test_result_has_required_keys) ... ok
#test_result_is_not_empty (tests.test_analyser.TestAnalyser.test_result_is_not_empty) ... ok
#test_total_students (tests.test_analyser.TestAnalyser.test_total_students) ... ok
#----------------------------------------------------------------------
#Ran 4 tests in 0.001s

#OK
import unittest
from analytics.analyser import TopStudentsAnalyser
class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample =[
            {"GPA": "4.0"}, {"GPA": "2.5"}, {"GPA": "4.0"}, 
            {"GPA": "1.8"}, {"GPA": "3.5"}
        ]
    def test_result_is_not_empty(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})
    def test_total_students(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)
    def test_result_has_required_keys(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("total_students", analyser.result)
        self.assertIn("high_performers", analyser.result)
    def test_analyse_twice(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)
if __name__ == '__main__':
    unittest.main()
