# String Art Generator

## Description

While getting bored in my class today I remembered this line art which my teacher ones taught me in school and start doodling on my tablet. I just thought it'd be interesting to see if I can write a program for it and hence this project. Here's what I came up with then:

<img src="images/doogle.jpg" alt="Image of a simple string art" width="500" height="800">

Now on to writing a script to do this. While the process itself is quite simple, we need to perform several calculations at every step so that the art stays cohesive. I am not motivated enough right now to explain the idea in great detail but I hope the code is able to communicate some of that.

## Commands

The drawer() function is the final result.

drawer(turtle, height, width, step_size, initial_angle, dir_y, dir_x)

turtle: Assumes you have defined a Turtle() object already and pass that here as an input.

height: Enter the height for your line art

width: Enter the width of your line art

step_size: Distance between two consecutive starting points on the same line. Keep it smaller for detailed drawings or larger for courser frameworks.

initial_angle: Allows you to set how much farther you want to go from the base in every iteration. It is adjusted in subsequent iteration so that the distance being covered on both lines in same in consecutive iterations.

The dir_x and dir_y assume that turtle is facing in east. Use command turtle.seth() to ensure that or play around with different orientations of the turtle.

dir_y: Set 0 if you want turtle to start along -y axis from its current position and 1 if you want to go towards +y axis to make the art.

dir_x: Set 0 if you want turtle to start along -x axis from its current position and 1 if you want to go towards +x axis to make the art.