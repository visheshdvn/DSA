from queue import LifoQueue

def checkBalanced(expr):
    q = LifoQueue()

    for i in expr:
        if i in ['(', '{', '[']:
            q.put(i)

        if i == '}':
            if q.empty() or q.get() != '{':
                return False

        if i == ']':
            if q.empty() or q.get() != '[':
                return False
        
        if i == ')':
            if q.empty() or q.get() != '(':
                return False

    return q.empty()

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

