# define a function to append string number into list
def return_of_list_numbers(number):
    n = str(number)
    list = []
    for i in range(len(n)):
        list.append(int(n[i]))
    return list

# define a number to append number into list without changing the data into string
def number_to_list_wo_string(number):
    numbers = []

    # find the max value of 10s
    n = 0
    while number / 10**n > 10.0:
        n += 1
    
    # add number to numbers
    for i in range(n,-1,-1):
        temp = number // 10**i
        numbers.append(temp)
        number = number - temp*10**i
    
    return numbers


number = int(input("Enter the number: "))

list_of_numbers = return_of_list_numbers(number)
# list_of_numbers = number_to_list_wo_string(number)

print(list_of_numbers)