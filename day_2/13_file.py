# Read is reading the whole fie
file = open("day_2/data1.txt", "r")

# Write is rewrite the whole file with a new data
file = open("day_2/data1.txt", "w")

# Append is adding a new data
file = open("day_2/data1.txt", "a")


# line = "sdfghj"
# while line != "":
#     line = file.readline()[:-1]
#     print(line)

file.writelines(["Fahmi", "Abdulaziz\n"])

file.close()