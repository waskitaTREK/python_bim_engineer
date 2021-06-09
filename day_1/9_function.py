def addNumber(num1, num2=1):
    res = num1 + num2
    return res

def mySum(numbers):
    res = 0

    for num in numbers:
        res = res + num
    
    return res

def factorial(number):
    res = 1

    for num in range(1,number+1):
        res = res * num
    
    return res

res = addNumber(7,22)

print(addNumber(9))
print(addNumber(9,40))

numbers = [1,2,3,4]
print(mySum(numbers))

print(factorial(10))