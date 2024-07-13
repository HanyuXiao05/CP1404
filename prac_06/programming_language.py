class ProgrammingLanguage:
    """a programming language object"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return a string of programming language information"""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'

    def is_dynamic(self):
        """return if a programming language is dynamic"""
        return True if self.typing == 'Dynamic' else False
