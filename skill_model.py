
class SkillModel

    def __init__(self):
        self.name = ""
        self.rank = -1
        self.description = ""

    def get_name(self):
        """Getter for name

        @return str the name of the skill
        """
        return self.name

    def set_name(self, name):
        """Setter for name

        @param name str the name of the skill
        @raises ValueError if name is not a string
        """
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Skill name was not a string.")

    def get_rank(self):
        """Getter for rank

        @return int the value of rank. -1 means untrained
        """
        return self.rank

    def set_rank(self, rank):
        """Setter from rank

        @param rank int value of the rank. -1 mean untrained
        @raises ValueError if rank is not an int
        """

        if type(rank) is int:
            self.rank = rank
        else:
            raise ValueError("Skill rank was not an int.")

    