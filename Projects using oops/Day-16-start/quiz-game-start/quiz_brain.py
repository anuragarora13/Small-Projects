class QuizBrain:
    def __init__(self,question_list):
        self.ques_num=0
        self.ques_list=question_list
    def still_has_questions(self):
        return self.ques_num < len(self.ques_list)
           
            
    def next_question(self):
        current_question=self.ques_list[self.ques_num]
        self.ques_num+=1
        input(f"{self.ques_num}: {current_question.text} (True/False): ")
   
        
            
           
    