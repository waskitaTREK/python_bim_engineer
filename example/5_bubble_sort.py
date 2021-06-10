numbers = [5,2,7,6,4,2,1,10,55,22,4,-5]

# for each data in the list based on the list length
for i in range(len(numbers)):
    # for each data in the list without checking the previous index and the last one
    for j in range(len(numbers) - i - 1):
        # if the value of data in index j is bigger than i
        # swapping
        if numbers[j] > numbers[j+1]:
            # define a variable to save index j data
            temp = numbers[j]
            # swap the data in index j into index j + 1
            numbers[j] = numbers[j+1]
            # move the data in temp into index j + 1
            numbers[j+1] = temp

print(numbers)