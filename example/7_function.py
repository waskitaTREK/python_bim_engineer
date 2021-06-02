def addByTwo(number):
    return number + 2

print(addByTwo(7))

def bubble_sort(numbers):
    is_sorted = False
    while(not is_sorted):
        is_sorted = True
        for i in range(len(numbers)):
            # if it's the end of list, than continue
            if i == len(numbers) - 1:
                continue
            
            # swapping
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp

                is_sorted = False
    
    return numbers


print(bubble_sort([2,5,3,1,2,99,443,23,42,5,64,5]))