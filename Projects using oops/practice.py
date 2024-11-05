# class Waiter:
#     is_holding_plate=False
#     tables_assigned=[]

#     def take_order():
#         print('tell menu to the customer')
#     def give_bill(self):
#         print('give bill')


# obj= Waiter()
# obj.give_bill()
# a=[1,2,3,4]
# b=a
# b.append(4)


# print(a)
# print(b)

# class Car:
#     def __init__(self,model,year):
#         self.model=model
#         self.year=year

# my_car = Car("Toyta",2024)  

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def greet(self):
#         return f"hello my name is {self.name} and i am {self.age} year old"    

# person1= Person("Anurag",25)
# print(person1.greet())   
        
           

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        return f"{self.name} \ {self.breed} says woof"
    

dog1=Dog('Bu ddy','Pitbull')
dog2=Dog('Max','German Shepherd')

print(dog1.bark())
print(dog2.bark())            
        
