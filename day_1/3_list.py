persn1 = "Taufiq"
persn2 = "Naufal"

persons = ["Taufiq", "Naufal", "Syamsul", "Yessy", "Ervan"]

persons[0] # accessing data

persons[0] = "Dedy" # changing list data

persons.insert(2,"Tohari")

print(persons)

persons.append("Akbar")
# print(persons)

persons.remove("Yessy")
# print(persons)

persons.pop(0)
# print(persons)

numbers = list(range(20))
print(numbers)
print(len(numbers))

# print(numbers[0:10])
# print(numbers[2:10])
# print(numbers[1:len(numbers):2])

list1 = list(range(10))
list2 = list(range(10,25))

list1.extend(list2)

print(list1)
