from ast import Str
from queue import LifoQueue


def infixToPostfix(exp):
    postfix = ""
    stack = LifoQueue()

    for i in exp:
        if i.isalpha() :
            postfix += i
            continue
        elif i == "(":
            stack.put(i)
        elif i == ")":
            pass
            


exp = input()
infixToPostfix(exp)
