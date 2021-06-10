number = int(input("Enter a number:"))

if number <= 1:
    print(str(number) + " is not prime number")

else:
    for divisor in range(2,number // 2):
        if number == 2:
            print(str(number) + " is prime number")
            break
        
        if number % divisor == 0:
            print(str(number) + " is not prime number")
            break
        
        if divisor == number - 1:
            print(str(number) + " is prime number")
            break

