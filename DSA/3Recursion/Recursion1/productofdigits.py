# get product of non 0 digits of a number

def get_product(n):
    if n == 0:
        return 1
    
    if n%10 == n:
        return n
    
    return (1 if n%10 == 0 else n%10) * get_product(n//10)

n = int(input("Enter the number: "))
print(get_product(n))