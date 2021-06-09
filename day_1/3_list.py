persn1 = "Taufiq"
persn2 = "Naufal"

persons = ["Taufiq", "Naufal", "Syamsul", "Yessy", "Ervan"]

persons[0] # accessing data

persons[0] = "Dedy" # changing list data

# insert data berdasarkan index, lalu memberikan isi data untuk index tersebut
persons.insert(2,"Tohari")

print(persons)

# menambahkan data pada list terakhir
persons.append("Akbar")
# print(persons)

# Menghilangkan data berdasarkan informasinya
persons.remove("Yessy")
# print(persons)

# Menghilangkan data berdasarkan indexnya
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
