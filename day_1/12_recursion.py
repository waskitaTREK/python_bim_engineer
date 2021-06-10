def printNumbersUntil0(number):
    print(number)

    number = number - 1
    if number > 0:
        printNumbersUntil0(number - 1)

# printNumbersUntil0(6)

def fibbonaci(index):
    # check if index is negative value
    if index < 0:
        print("please insert non negative integer")
        return
    
    # check if index is 0 or 1
    if index in [0,1]:
        return index
    
    # call recursion
    else:
        return fibbonaci(index - 1) + fibbonaci(index - 2)

def faster_fib(index, mem={}):
    if index < 0:
        print("please insert non negative integer")
        raise Exception("err")
    
    # check if index is 0 or 1
    if index in [0,1]:
        return index
    
    elif index not in mem.keys():
        mem[index] = faster_fib(index - 1,mem) + faster_fib(index - 2,mem)
    
    return mem[index]

print(faster_fib(45))