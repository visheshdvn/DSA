def checkRedundancy(Str): 
	st = []

	for ch in Str: 
		if (ch == ')'): 
			top = st.pop()

			flag = True

			while (top != '('): 

				if (top == '+' or top == '-' or top == '*' or top == '/'): 
					flag = False

				top = st.pop()

			if (flag == True): 
				return True
                
		else: 
			st.append(ch)
	return False

string = input()
ans = checkRedundancy(string)
if ans is True:
    print('true')
else:
    print('false')

