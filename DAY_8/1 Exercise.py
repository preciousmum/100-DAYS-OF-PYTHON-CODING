'''The challenge today is to create a program that helps you calculate how many
cans of paint you need for a given surface of wall '''
import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height*width)/cover)
    print (f"You'll need {num_of_cans} to completely paint the wall")




test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
