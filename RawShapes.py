from turtle import *

import math



# Name your Turtle.

t = Turtle()



# Set Up your screen and starting position.

setup(500,300)

x_pos = -250

y_pos = -150

t.setposition(0, 0)



### Write your code below:
color = input("Enter a color:")
pencolor(color)

fillcolor(color)
begin_fill()


pendown()
numberOFSides = input("Enter a number:")
for shape in range(int(numberOFSides)):
    forward(50)
    right(360/(int(numberOFSides)))

end_fill()














# Close window on click.

exitonclick()
