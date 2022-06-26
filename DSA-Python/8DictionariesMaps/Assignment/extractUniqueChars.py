# Question)Given a string, you need to remove all the duplicates. That means, 
# the output string should contain each character only once. The respective order of characters should remain same.

# Constraints :
# 0 <= Length of S <= 10^8

# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd

def uniqueChars(string):
    nstr = ''
    for i in string:
        if i not in nstr:
            nstr += i

    return nstr

# Main
string = input()
print(uniqueChars(string))
