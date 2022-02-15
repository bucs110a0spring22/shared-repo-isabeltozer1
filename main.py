
import turtle

number_of_sides= int(input("Enter number of sides"))
length_of_each_side = int(input("Enter length of each side"))
henry = turtle.Turtle()
henry.color("yellow")

for i in range(number_of_sides):

   henry.forward(length_of_each_side)
   henry.left(360/number_of_sides)

Window = turtle.Screen()
Window.bgcolor("orange")
Window.exitonclick()
