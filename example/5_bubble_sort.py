numbers = [5,2,7,6,4,2,1,10,55,22,4]

for i in range(len(numbers)):
    is_sorted = True
    for j in range(len(numbers) - i):
        # if it's the end of list, than continue
        if j == len(numbers) - 1:
            continue
        
        # swapping
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

            is_sorted = False

print(numbers)