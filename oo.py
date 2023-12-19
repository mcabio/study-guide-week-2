# Part 1: Classes and Init Methods
# Make 3 Python classes that could store student, question, and exam information
# Use the tables as examples to guide you in creating class definitions for the following objects. 
# Define an __init__ method to allow callers of this class to provide initial values for 
# each attribute. Note: these classes should not be a subclass of any other.

class Student:
    """Student class"""
    def __init__(self, first_name, last_name, address):
        """Initialize student."""
        self.first_name = first_name # These values need to be in the same order 
        self.last_name = last_name   #listed in the parameters (parenthesis)
        self.address = address
        

class Question:
    """Question class"""
    def __init__(self, question, correct_answer):
        """Initializes questions"""
        self.question = question
        self.correct_answer = correct_answer

    # The __str__ method is defined to provide a string representation of the question and correct answer.
    # The __str__ method is a special method that is used to define the "informal" or "user-friendly" 
    # string representation of an object. When you use the print function or the str() function 
    # on an object, Python internally calls the object's __str__ method to obtain the string representation.
    def __str__(self):
        return f"Question: {self.question}\nCorrect Answer: {self.correct_answer}"
    
    # Add a method called ask_and_evaluate to the Question class. This method should 
    # print the question to the console and prompt the user for an answer. 
    # It should then return True or False depending on whether the correct answer matches the user’s answer. 
      
    def ask_and_evaluate(self):
        """Prints the question, prompts the user for an answer, and evaluates it."""
        print(self.question)
        user_answer = input("Your answer: ")
        return user_answer == self.correct_answer

# Exam should have an attribute called questions. 
# Simply initialize the questions attribute as an empty list in the body __init__ function. 
# Your __init__ function should take a name for the exam as a parameter.
    
class Exam:
    """Exam class"""
    def __init__(self, name):
        """Initializes exam name and exam questions"""
        self.name = name
        # Notice how questions is not included as a parameter in the __init__ method's 
        # parenthesis, It's because it's initialized as an empty list directly within the method body. 
        # This line initializes the questions attribute as an empty list. 
        # By initializing it within the method body rather than as a parameter, 
        # you allow the class to have a default behavior of starting with an empty 
        # list of questions when an Exam object is created.
        # Including questions as a parameter in the __init__ method could be done 
        # if you wanted to provide an initial list of questions when creating an Exam instance. 
        # However, in this case, it seems the design choice is to start with an empty list 
        # and allow questions to be added later using the add_question method.
        self.questions = [] 

    # This method is defined for the Exam class to provide a string representation of an Exam object.
    # question_names: This line creates a string that contains all the questions in the exam, 
    # separated by commas. It uses a generator expression and the join method to 
    # concatenate each question in self.questions.
    def __str__(self):
        # generator expession is (question.question for question in self.questions).
        # ', ' <-- This is what will separate the question string from each other. 
        # .join is the method that puts the question strings together. The period between question.question 
        # is part of the attribute access syntax in Python. It is used to access the attribute 
        # named question of each question object in the iterable self.questions.
        #  It is specifying that you are accessing the question attribute of each question object.
        question_names = ', '.join(question.question for question in self.questions)
        return f"Exam: {self.name}\nQuestions: {question_names}" # This would output this result: 
                                                                 # Exam: Midterm
                                        # Questions: What is the capital of Alberta?, Who is the author of Python?


    
# Add a method called add_question to the Exam class which takes a Question 
# and adds it to the exam’s list of questions.
    
    def add_question(self, question):
        self.questions.append(question)

# Create administer method inside Exam class. Initialize a variable called score --- set it to zero
# loop through each of the questions in the exam for each question, call the question's method
# ask_and_evaluate if it returns True, increment score calculate and return the percentage score.
        
    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score +=1

        percentage_score = (score / len(self.questions)) * 100
        return f"You scored {percentage_score} on your exam."

class Quiz(Exam): # This inherits from the Exam class.
    """Quiz class, inherits from Exam."""
    def __init__(self, name):
         super().__init__(name)

# However, whereas exams are given a percentage score, quizzes are pass/fail. 
# If you answered at least half of the questions correctly, you pass the quiz; 
# otherwise, you fail. When you call the administer method on a quiz, it should 
# return 1 if you passed or 0 if you failed.
         
    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        
        # Determine pass or fail based on the number of correct answers
        if score >= len(self.questions) / 2:
            return 1  # Passed
        else:
            return 0  # Failed

# Write a class called StudentExam that has two methods: __init__ and take_test. 
# This class should be able to store a student, an exam, and the student’s score for that exam. 
        
class StudentExam:
    def __init__(self, student, exam, student_score=None): # The student_score=None parameter provides 
                                                    # a default value for the student_score attribute.  
                                                    # This means that if the student_score argument is not 
                                                    # provided when creating an instance of the StudentExam class, 
                                                    # the default value of None will be assigned.
        self.student = student
        self.exam = exam
        self.student_score = student_score

# The take_test method administers the exam and assigns the actual score 
# to the StudentExam instance. This method should also print a message to the 
# screen indicating the score; a return value isn’t required.   
        
    def take_test(self):
        self.student_score = self.exam.administer()
        print(f"Student {self.student} scored {self.student_score} on the exam.")

class StudentQuiz(StudentExam):
    """StudentQuiz class, inherits from StudentExam."""

    def take_test(self):
        super().take_test()
        result = "passed" if self.student_score == 1 else "failed"
        print(f"Student {self.student} {result} the quiz.")

# Now, write a function (not a method) called example, which does the following:
# Creates an exam
# Adds a few questions to the exam
# These should be part of the function; no need to prompt the user for questions.
# Creates a student
# Instantiates a StudentExam, passing the student and exam you just created as arguments
# Administers the test for that student using the take_test method you wrote
def example():
    # Create an Exam object
    exam = Exam("Final Exam")

    # Add questions to the exam
    question1 = Question("What is the capital of Alberta?", "Edmonton")
    question2 = Question("Who is the author of Python?", "Guido Van Rossum")

    exam.add_question(question1)
    exam.add_question(question2)

    # Create a StudentExam object
    student_exam = StudentExam("John Doe", exam)

    # Take the exam
    student_exam.take_test()

    # Create a Quiz object
    quiz = Quiz("Quiz")

    # Add questions to the quiz
    question3 = Question("What is 2 + 2?", "4")
    question4 = Question("Which programming language is known for its simplicity?", "Python")

    quiz.add_question(question3)
    quiz.add_question(question4)

    # Create a StudentQuiz object
    student_quiz = StudentQuiz("John Doe", quiz)

    # Take the quiz
    student_quiz.take_test()

if __name__ == "__main__":
    example()
