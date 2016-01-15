import csv
import model


def load_questions(session): #fix float to import
    with open('questions.csv', 'rU') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', dialect=csv.excel_tab)
        for field in datareader:
            new_question = model.Question(
                strand_id = field[0],
                strand_name = field[1],
                standard_id = field[2],
                standard_name = field[3],
                question_id = field[4],
                difficulty = field[5])

            session.add(new_question)

def load_students(session): 
    with open('usage.csv', 'rU') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', dialect=csv.excel_tab)
        for field in datareader:
            new_student = model.Students(
            student_id = field[0],
            question_id = field[1],
            assigned_hours_ago = field[2],
            answered_hours_ago = field[3])

            session.add(new_student)



def main(session):
    load_questions(session)
    load_students(session)

    session.commit()

if __name__ == "__main__":
    session = model.connect()
    session = model.db_session
    main(session)