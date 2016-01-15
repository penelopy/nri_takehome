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

#Import CSV to Database (possibly use cache or in-memory db)? Use classes

class Question:
    def __init__(self, strand_id, strand_name, standard_id, standard_name, question_id, difficulty):
        self.strand_id = strand_id 
        self.strand_name = strand_name
        self.standard_id = standard_id 
        self.standard_name = standard_name
        self.question_id = question_id 
        self.difficulty = difficulty

    def select_record_by_strand(self):
        pass

    def select_record_by_name(self):
        pass

#Ask for user input (input needs to be integer > 0)
num_questions = input("How many questions would you like?")

#Select questions to display (equal number of strands, equal number of standards)

#Display a list of question IDs

