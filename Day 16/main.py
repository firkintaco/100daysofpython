#import turtle
#from turtle import Turtle, Screen

#my_screen = Screen()
#my_screen.title("Hehehehe kilpikonna")
#print(my_screen.bgcolor())

#my_screen.bgcolor("black")
#timmy = Turtle()
#karpo = Turtle()

#karpo.color("lawngreen")
#timmy.shape("turtle")
#timmy.color("DeepPink1")
#karpo.shape("turtle")
#karpo.left(180)
#for i in range(10,50):
 #   timmy.forward(100)
#    karpo.forward(100)
#    timmy.left(i*5)
 #   karpo.left(i * 5)

#my_screen.exitonclick()
from prettytable import PrettyTable

pokemons = ["Pikachu", "Squirtle", "Charmander"]
pokemon_types = ["Electric", "Water", "Fire"]
table = PrettyTable()
table.add_column("Pokemon name", pokemons)
table.add_column("Type", pokemon_types)
table.align = "r"
print(table)