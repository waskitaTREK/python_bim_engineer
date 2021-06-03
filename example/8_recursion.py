# Python program to display the Fibonacci sequence

# usual fibbonaci
def fibonacci(n):
    # check if number not negative
    if n < 0:
        raise Exception("Please insert positive integer")
    
    # if number is 0 or 1, return the number
    if n <= 1:
        return n

    # do the recursion
    return fibonacci(n-1) + fibonacci(n-2)

# faster fibbonaci
def faster_fib(n, mem={}):
    # check if number not negative
    if n < 0:
        raise Exception("Please insert positive integer")
    
    # if number is 0 or 1, return the number
    if n <= 1:
        return n
    
    # add calculated number to memory
    if n not in mem.keys():
        mem[n] = faster_fib(n-1, mem) + faster_fib(n-2, mem)

    # return the number from memory
    return mem[n]

n = int(input("Enter a number: "))

print(fibonacci(n))

print(faster_fib(n))