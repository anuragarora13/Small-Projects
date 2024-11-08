# from turtle import Turtle,Screen

# timmy=Turtle()

# print(timmy)

# timmy.shape("turtle")

# timmy.color("coral")

# my_screen=Screen()

# timmy.forward(500)

# my_screen.canvheight

# my_screen.exitonclick() 


# from  prettytable import PrettyTable

# table=PrettyTable()

# table.add_column("Pokemon name",["Pickachu","Squirtle","Cahrmander"])

# table.add_column("Pokemon Type",["Electric","Water","Fire"])

# table.align='l'
# print(table)

# class Courses:
    
#     def __init__(self,total_semester,faculty_count):
#         self.total_semester=total_semester
#         self.faculty_count=faculty_count
        

        
# mba= Courses(4,30)
# mca=Courses(4,20)
# class User:
#     pass
    
# print("hello")    
# user1=User()          

# def myfunction():
#     pass


# class Person:
#     def __init__(self,name,age,car):
#         self.name=name
#         self.age=age
#         self.ca=car

#     def introduce(self):
#         print(f'my name is{self.name} and my age is {self.age} and i have a car {self.ca} ')    

# person1 = Person('varun',22,"Toyta")
# person1.introduce()

class User:    
    def __init__(self,user_id,username):
        self.id=user_id
        self.name=username
        self.followers=0
        self.following_count=0
        
        
    def follow(self,user):
        user.followers+=1
        self.following_count+=1        
            
         
user1=User("001","angela")
user2=User("002","jack")        


user1.follow(user2)
print(user1.followers)
print(user2.followers)








