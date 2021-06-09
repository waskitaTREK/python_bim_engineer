words = ["hello", "waskita", "dan", "wbp"]

tup = ("hello", "waskita", "dan", "wbp")

a, b = (5, 10)

a, b = b, a

words[0], words[1] = words[1], words[0]

# print(a, b)
# print(words)

# dictionary

persons = [
    {"nama": "fahmi", "alamat":"Bekasi"},
    {"nama": "yessy", "alamat":"Citayeum"},
    {"nama": "marsa", "alamat":"Tebet"}
]

print(persons[0]["alamat"])