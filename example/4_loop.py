# "For" Loop
## Loop item value
fruits = ["mango","pineapple","orange","apple"]
for x in fruits:
    print(x)

## Loop item using its index numbers
for i in range(len(fruits)):
    print("index " + str(i) + ": " + fruits[i])

# "While" Loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1

# Break and Continue Loop
## Continue
company = "Waskita"
for letter in company:
    if letter == "i":
        continue
    print("Letter: ", letter)
## Break
for letter in company:
    if letter == "i":
        break
    print("Letter: ", letter)