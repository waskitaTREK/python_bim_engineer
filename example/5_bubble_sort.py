numbers = [5,2,7,6,4,2,1,10,55,22,4,-5]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        # swapping
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

print(numbers)