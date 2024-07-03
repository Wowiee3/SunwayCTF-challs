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
        return "<redacted>"


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


print("--- Write your code below (Ctrl + D to end) ---")
source_code = ""
for line in stdin:
    source_code += line

tree = parse(source_code)
if analyse(tree):
    main_ast.body += tree.body
    print("Your code looks safe! Now executing...")
    compiled = unparse(main_ast)
    exec(compiled)
else:
    print("Hey! Back off! That's my locker!")
