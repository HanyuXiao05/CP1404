class Band:
    def __init__(self, name):
        """A band object."""
        self.name = name
        self.members = []

    def __str__(self):
        """return a string of band information"""
        member_string = ', '.join([f'{member.name} ({member.instruments})' for member in self.members])
        return f'{self.name} ({member_string})'

    def add(self, member):
        """add new member to band object"""
        self.members.append(member)

    def play(self):
        """all members play instruments"""
        return '\n'.join([member.play() for member in self.members])
