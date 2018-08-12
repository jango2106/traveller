from die import Die
import re

class DieRoller:

    def __init__(self):
        """Constructor"""
        self.die = Die()
        self.CHARACTERISTICS = 6

    
    def roll_die(self, first, sides=None, *mod_list):
        """Rolling a die given number, die sides, and mods

        One Parameter:
            @param first str "xdy +/- z" pattern with x being the number
            of die to roll, y being die sides, and z being additional modifiers
        2 or 3 Parameters:
            @param first int number of die to be rolled
            @param sides int number of sides of the die to be rolled
            @param *mod_list int additional mods to add to the roll  

        """
        num_of_rolls = 0 
        die_sides = 0
        mods = list()
        roll = 0

        if type(first) is str:
            num_of_rolls, die_sides, mods = self.__generate_die_roll_from_string(first)
        else:
            num_of_rolls = first
            die_sides = sides
            if len(mod_list) > 0 and type(mod_list[0]) is list:
                mods = mod_list[0]
            else:
                mods = mod_list
        
        self.die.set_sides(die_sides)

        #rolls the die a number of times
        for i in range(num_of_rolls):
            roll += self.die.roll()

        #adds or subtracts modifiers
        for mod in mods:
            roll += mod

        return roll

    def roll_characteristics(self):
        """Roll for all characteristics. Each is a 2d6 roll

        @return list int values to be assigned to characteristics
        """
        rolls = list()

        for i in range(self.CHARACTERISTICS):
            rolls.append(self.roll_die(2,6))

        return rolls


    def __generate_die_roll_from_string(self, value):
        """Take in a string in the form of xdy + z... and give back values that 
        can be used in the roll_die()

        @return tuple
            @value int the number of dice to be rolled
            @value int the number of sides the dice to be rolled has
            @value list positive and negative modifiers to be added
        """

        #Checks for the xdy +/- z... format. Ex 1d6 + 6 - 2
        if not re.match(r"^\d+\s*[dD]\s*\d+(\s*[+-]\s*\d+)*$", value):
            raise ValueError("Die roll was not entered in a xdy +/- z ... format")

        #removes whitspace chars from the input
        roll = re.sub(r'\s','', value)

        #splits input by digits to separate out param values
        roll_params = re.split(r'\d', roll)

        #Removes random '' characters in the 0th and -1st positions from re.split()
        roll_params.pop(0)
        roll_params.pop(-1)

        #splits input by non digits to separate out values
        roll_values = re.split(r'\D', roll)

        mods = list()

        #iterates though mod values and adds the right pos/neg version to mods
        #list to return
        for value in range(2,len(roll_values)):
            identifier = roll_params[value - 1]
            if identifier == '+':
                mods.append(int(roll_values[value]))
            elif identifier == "-":
                mods.append(int(roll_values[value]) * -1)
                
        return (int(roll_values[0]), int(roll_values[1]), mods)

roller = DieRoller()
print(roller.roll_characteristics())