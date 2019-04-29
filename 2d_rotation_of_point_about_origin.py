import math
from math import *
import sys

""" 2D rotation of a given point about the origin """
def new_point(x,y,angle):
    rad  = sqrt(x^2 + y^2)
    old_angle = degrees(math.asin(x/y))
    new_angle = angle + old_angle
    print('old_angle:', old_angle)
    print('new_angle:', new_angle)
    new_x = rad*(cos(radians(new_angle)))
    new_y = rad*(sin(radians(new_angle)))
    return new_x, new_y

if __name__ == "__main__":
    if not len(sys.argv) > 3: 
        print("Usage: 2d_rotation_of_point_about_origin.py x_cord y_cord angle")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        angle = int(sys.argv[3])
        x,y = new_point(x,y,angle)
        print('After 2D transformation X is {} and Y is {}'.format(x,y))
