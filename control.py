
import datetime
import model

#Import CSV to Database (possibly use cache or in-memory db)? Use classes

#Ask for user id (this information will be used to select question and track data)
user_id = input("Please input your user id")

#Ask for user input (input needs to be integer > 0)
num_questions = input("How many questions would you like?")

#Determine current time and record in database
time = datetime.now()


def select_unanswered_question():
    #Retrieve data about student by querying db 
    assigned_questions = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    new_questions_for_user = []
    user_data = model.db_session.query(model.Student).filter_by(student_id=user_id).all()
    for question in user_data.question_id: 
        assigned_questions[question] = assigned_questions(question) + 1 
    for key, value in assigned_questions: 
        if value == 0: 
            new_question = assigned_questions[key]
            new_questions_for_user.append(new_question)
            num_questions += 1
    return new_questions_for_user


#Select questions to display (equal number of strands, equal number of standards)
def select_record_by_strand(self):
    possible_questions = select_unanswered_question()
    #TODO determine type of questions and select new standard/strand

def select_record_by_name(self):
    pass

#Display a list of question IDs

