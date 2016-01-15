"""* The program should prompt the user for the number of questions to put in the quiz. 
Any integer value greater than 0 is acceptable.
* The expected output is to display a list of question_ids
* Use each strand as close as possible to an equal number of times. (e.g. 
    There are two strands, so if the user asks for a 3 question quiz, it's okay 
    to choose one strand twice and the other once.)
* Use each standard as close as possible to an equal number of times.
* Duplicating questions in the quiz is OKAY!
* Not completing the basic requirements IS NOT FAILURE.  We'd rather see a 
beautiful attempt than a complete attempt.
* Please use git to track progress. E.g. progressively commit changes so we 
can track your thought process."""

import datetime

#Import CSV to Database (possibly use cache or in-memory db)? Use classes

#Ask for user id (this information will be used to select question and track data)
user_id = input("Please input your user id")

#Ask for user input (input needs to be integer > 0)
num_questions = input("How many questions would you like?")

#Determine current time and record in database
time = datetime.now()

#Retrieve data about student by querying db 

#Select questions to display (equal number of strands, equal number of standards)
def select_record_by_strand(self):
    pass

def select_record_by_name(self):
    pass
#Display a list of question IDs

