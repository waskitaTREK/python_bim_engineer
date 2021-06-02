def addByTwo(number):
    return number + 2

print(addByTwo(7))

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            # swapping
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    
    return numbers


print(bubble_sort([2,5,3,1,2,99,443,23,42,5,64,5]))