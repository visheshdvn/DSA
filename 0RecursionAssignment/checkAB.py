# def checkab(str, ind):
#     result = True
#     if str[0] != 'a':
#         return False
    
#     if ind > len(str):
#         return None
    
#     if str[ind] == 'a':
#         if str[ind +1] == 'a':
#             return True or checkab(str, ind+1)
#         if str[ind+1:ind+3] == 'bb':
#             return True or checkab(str, ind +1)
    
#     if str[ind: ind+2] == 'bb' and str[ind+2] == 'a':
#         return True or checkab(str, ind+2)
        
    
def checkab(str, chars, ind):
    if len(str) <= ind:
        return True
    
    if str[ind] in chars:
        return True and checkab(str, ['a', 'bb'], ind+1)
    
    elif str[ind: ind+2] in chars:
        return True and checkab(str, ['a'], ind+2)
    
    return False

str = input()
if checkab(str, ['a'], 0):
    print('true')
else:
    print('false')
