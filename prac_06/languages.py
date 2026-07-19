"""
CP1404 Week 6 Practical - intermediate exercise
Programming language client code.
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programming_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
print("\n".join([language.name for language in programming_languages if language.is_dynamic()]))

#print(python)