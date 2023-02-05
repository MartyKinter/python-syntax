def print_upper_words(words):
    ''' Prints each word in list uppercase'''

    for word in words :
        print(word.upper())

def print_upper_words2(words):
    '''prints only words starting with "e" or "E" to uppercase'''

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with)
    '''print words in uppercase that start with specified letters'''

    for word in words
        for letter in must_start_with
            if word.startswith(letter)
                print(word.upper())
                break