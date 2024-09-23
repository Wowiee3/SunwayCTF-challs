from ast import *
from sys import stdin

BANNED = (Import, ImportFrom, Call, FunctionDef, Lambda, ClassDef, AsyncFunctionDef)
CONTEXT = """
from dataclasses import dataclass


class Locker:
    pass


@dataclass(frozen=True)
class SunLocker(Locker):
    def __flag(self):
        return "sunctf{m4Rv3l0u5_pY7h0N_5Ki115}"


class PublicLocker(Locker):
    def __init__(self):
        print("Welcome!")


locker = PublicLocker()
"""
main_ast = parse(CONTEXT)


def analyse(m):
    for x in walk(m):
        if type(x) in BANNED:
            return False
    return True


print("--- Write your code below (Type 'end' (without quotes) in a newline to end your input) ---")
source_code = ""
while True:
    line = input()
    if line == 'end':
        break
    source_code += line + '\n'

try:
    tree = parse(source_code)
    if analyse(tree):
        main_ast.body += tree.body
        print("Your code looks safe! Now executing...")
        compiled = unparse(main_ast)
        exec(compiled)
    else:
        print("Hey! Back off! That's my locker!")
except:
    print("An error occurred while executing your code.")
