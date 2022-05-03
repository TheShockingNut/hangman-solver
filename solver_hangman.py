from nltk.corpus import words

word_list = words.words()
letters_contained = []
starts_with = ''
ends_with = ''
not_contains = []
somewhere = ''
leng = 0
index = 0

def contains(letters):
    global letters_contained
    for letter in letters_contained:
        if letter not in letters:
            return False
    return True

def starts_with_check(letters):
    global starts_with
    if letters.startswith(starts_with):
        return True
    return False

def ends_with_check(letters):
    global ends_with
    if letters.endswith(ends_with):
        return True
    return False

def not_contains_check(letters):
    global not_contains
    for letter in not_contains:
        if letter in letters:
            return False
    return True

def somewhere_check(letters):
    global somewhere
    global index
    if somewhere in letters[index:]:
        return True
    return False

def leng_check(letters):
    if len(letters) == leng:
        return True
    return False

if __name__ == '__main__':
    for word in word_list:
        word = word.lower()
    
    print("Please enter the letters that are contained in the word:")
    letters_contained = list(input())

    print("Please enter the letters that are not contained in the word:")
    not_contains = list(input())

    print("Please enter the letters that are in the beginning of the word:")
    starts_with = str(input())

    print("Please enter the letters that are in the end of the word:")
    ends_with = str(input())

    print("Please enter the letters that are somewhere in the word:")
    somewhere = str(input())
    if somewhere is not None:
        print("Please enter the first index of the letter:")
        index = int(input())

    print("Please enter the length of the word:")
    leng = int(input())

    if letters_contained is not None:
        obj1 = list(filter(contains,word_list))

    if starts_with is not None:
        obj1 = list(filter(starts_with_check,obj1))

    if ends_with is not None:
        obj1 = list(filter(ends_with_check,obj1))

    if not_contains is not None:
        obj1 = list(filter(not_contains_check,obj1))
    
    if somewhere is not None:
        obj1 = list(filter(somewhere_check,obj1))

    if leng is not 0:
        obj1 = list(filter(leng_check,obj1))
    
    print(obj1)