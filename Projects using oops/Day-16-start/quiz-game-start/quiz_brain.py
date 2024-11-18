class QuizBrain:
    def __init__(self,question_list):
        self.ques_num=0
        self.ques_list=question_list
        self.score=0
    def still_has_questions(self):
        return self.ques_num < len(self.ques_list)
            
    def next_question(self):
        current_question=self.ques_list[self.ques_num]
        self.ques_num+=1
        user_answer=input(f"{self.ques_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score+=1
        else:
            print('Thats Wrong')
        print(f"The correct answer was: {correct_answer}  ")        
        print(f"your current score is {self.score}/{self.ques_num} ")    
        print() 
        
        
            
           
    