def get_number_of_digits(n):
    n = abs(n)
    
    count = 0

    while n != 0:
        count +=1
        n//=10
    
    return count

n = int(input("Enter a number: "))
print("Number of digits = ", get_number_of_digits(n))