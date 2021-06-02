numbers = [5,2,7,6,4,2,1,10,55,22]

is_sorted = False
while(not is_sorted):
    is_sorted = True
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            continue
        
        # swapping
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp

            is_sorted = False

print(numbers)