number = int(input("Enter a number:"))

for divisor in range(2,number):
    if number == 2:
        print("prime number")
        break

    if number % divisor == 0:
        print("not prime number")
        break
    
    if divisor == number - 1:
        print("prime number")
        break

