from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

ProgrammingLanguage = [python, ruby, visual_basic]
DynamixProgrammingLanguage = [i for i in ProgrammingLanguage if i.is_dynamic()]
print('The dynamically typed languages are:')
for lang in DynamixProgrammingLanguage:
    print(lang.name)
