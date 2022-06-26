# Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. You need to find the minimum number of bracket reversals which are required to make the expression balanced.

# Sample Input 1 :
# {{{
# Sample Output 1 :
# -1
# Sample Input 2 :
# {{{{}}
# Sample Output 2 :
# 1

def countMinReversals(expr): 

	l = len(expr)

	if (l % 2):
		return -1

	s = [] 
	for i in range(l): 
		if (expr[i] =='}' and len(s)): 

			if (s[0] == '{') : 
				s.pop(0) 
			else: 
				s.insert(0, expr[i]) 
		else: 
			s.insert(0, expr[i]) 
	
	# Length of the reduced expression 
	# red_len = (m+n) 
	reml = len(s) 

	# count opening brackets at the 
	# end of stack 
	n = 0
	while (len(s) and s[0] == '{') : 
			s.pop(0) 
			n += 1

	# return ceil(m/2) + ceil(n/2) which 
	# is actually equal to (m+n)/2 + n%2 
	# when m+n is even. 
	return (reml // 2 + n % 2) 

expr = input()
print(countMinReversals(expr.strip()))