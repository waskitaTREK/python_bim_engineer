# input list
words = ["Hello", "BIM", "Engineer", "UB"]

# find the maximum number of word length
max_width = 0
for word in words:
    if len(word) > max_width:
        max_width = len(word)

# print top border
print('*' * (max_width + 4))

# print words with side border
for word in words:
    print('* ' + word + ' '*(max_width-len(word)) + ' *')

# print bottom border
print('*' * (max_width + 4))