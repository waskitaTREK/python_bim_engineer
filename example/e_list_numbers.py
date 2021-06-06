def return_of_list_numbers(number):
    list = []
    for i in range(len(number)):
        list.append(int(number[i]))
    return list

input = input("Enter the number: ")

list_of_numbers = return_of_list_numbers(input)

print(list_of_numbers)