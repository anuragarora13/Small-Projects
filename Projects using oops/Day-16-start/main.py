# from turtle import Turtle,Screen

# timmy=Turtle()

# print(timmy)

# timmy.shape("turtle")

# timmy.color("coral")

# my_screen=Screen()
# timmy.forward(500)
# my_screen.canvheight
# my_screen.exitonclick() 


from  prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon name",["Pickachu","Squirtle","Cahrmander"])
table.add_column("Pokemon Type",["Electric","Water","Fire"])
table.align='l'
print(table)