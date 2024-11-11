from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question(question_text,question_answer)  
    question_bank.append(new_question)
    




qustion_list=QuizBrain(question_bank)

while qustion_list.still_has_questions():
    qustion_list.next_question()
    

    
