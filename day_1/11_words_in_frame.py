words = ["Hello", "some", "waskita karya"]

def wordsInFrame(words):
    # get max number of char count
    maxWidth = 0
    for word in words:
        if maxWidth < len(word):
            maxWidth = len(word)
    
    # top frame
    print('*' * (maxWidth + 4))

    # words with side frame
    for word in words:
        print('* ' + word + ' '*(maxWidth - len(word)) + ' *')

    # bottom frame
    print('*' * (maxWidth + 4))

wordsInFrame(words)