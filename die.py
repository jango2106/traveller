'''
A class to hold data associated with a die.
@Author Dustin Roan (dustin.a.roan@gmail.com)
@Version 8/12/2018
'''

import random

class Die:

    """Defalut constructor of a die.
    @param sides int The number of sides a die has. Default is 6
    @raises ValueError if sides param is not an integer
    """
    def __init__(self, sides=6):
        if type(sides) is int:
            self.sides = sides
        else:
            print("Die 'sides' var can only take int type arguements")
            raise ValueError 

    """Simulate rolling a die of x sides.
    @return int the value of the roll
    """
    def roll(self):
        return random.randint(1,self.sides)

    def set_sides(self, sides):
        self.sides = sides