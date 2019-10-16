#!/usr/bin/env python3

# Added name to print.
print("My name: Omer")

# Added favorite color to print
print("My favorite color: Green")

# Defining variable fav_activity
fav_activity = 'Science'

# Added favorite activity to print
print("My favorite activity:" , fav_activity)

# Added favorite animal to print
print("My favorite animal: Cheetah")

# Create blank space variable
blank_space = ' '

# Create space
print(blank_space)
# Added bellow phrase to print
print("Trying to use sys.argv")
# Create space
print(blank_space)

import sys

# Define Name, Color, Activity, Animal
name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

# Added sys variables to print
print("My name:" , name)
print("My favorite color:" , color)
print("My favorite activity:" , activity)
print("My favorite animal:" , animal)

