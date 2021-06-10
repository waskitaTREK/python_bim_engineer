file = open("day_2/data1.txt", "a")


# line = "sdfghj"
# while line != "":
#     line = file.readline()[:-1]
#     print(line)

file.writelines(["Fahmi", "Abdulaziz\n"])

file.close()