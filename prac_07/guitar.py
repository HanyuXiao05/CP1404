YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """a guitar object"""

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """return a string of guitar information"""
        return f'{self.name} ({self.year}) : ${self.cost:.2f} added.'

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """get the age of the guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """return if a guitar is vintage"""
        return self.get_age() >= VINTAGE_YEAR
