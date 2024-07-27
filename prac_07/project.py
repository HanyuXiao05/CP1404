MAXIMUM_PERCENTAGE = 100


class Project:
    """A project object."""
    def __init__(self, name='', start_date='', priority=0, cost_estimate=0, completing_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completing_percentage = completing_percentage

    def __lt__(self, other):
        """less than method for the object"""
        return self.priority < other.priority

    def __str__(self):
        """string method for the object"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completing_percentage}%")

    def is_complete(self):
        """Determine if a projest is complete."""
        return self.completing_percentage == MAXIMUM_PERCENTAGE
