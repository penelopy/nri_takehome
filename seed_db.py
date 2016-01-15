import csv
from control import Question


def load_questions(session):
    with open('questions.csv', 'rU') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', dialect=csv.excel_tab)
        for field in datareader:


        new_question = control.Question(
            self.strand_id = field[1]
            self.strand_name = field[2]
            self.standard_id = field[3]
            self.standard_name = field[4]
            self.question_id = field[5]
            self.difficulty = field[6])
