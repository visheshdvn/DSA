def fizzBuzz(n):
    arr = [str(i) for i in range(1, n+1)]
    
    for i in range(2, n, 3):
        arr[i] = "Fizz"
        
    for i in range(4, n, 5):
        arr[i] = "Buzz"
        
    for i in range(14, n, 15):
        arr[i] = "FizzBuzz"
    
    return arr


n = int(input())
print(fizzBuzz(n))
