number = 5

numbers = [1,2,3,4,5]

# if statement
if number == 5:
    print(number)

if len(numbers) == 5:
    print(numbers[3])

if number in numbers: # if 3 in [1,2,3,4,5]
    print("3 is here")

# elif and else statement
if number == 3:
    print("is 3")
elif number == 5:
    print("is 5")
else:
    print("not 3 & 5")