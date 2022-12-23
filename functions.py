import random


## Getting list of possible words

def get_words():
    with open('words.txt', 'r') as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.append(line.strip('\n'))
        return words


## Lowering all words to lowercase

def lower_case(words):
    words2 = []
    for word in words:
        words2.append(word.lower())
    return words2


## Spliting words in separate lists based on length

def words_split(words):
    word_groups = {'words3': [], 'words4': [], 'words5': [], 'words6': [], 'words7': [], 'words8': [],
                   'words9': [], 'words10': [], 'words11': [], 'words12': []}

    for x in words:
        if len(x) == 3 and x.isalpha():
            word_groups['words3'].append(x)
        if len(x) == 4 and x.isalpha():
            word_groups['words4'].append(x)
        if len(x) == 5 and x.isalpha():
            word_groups['words5'].append(x)
        if len(x) == 6 and x.isalpha():
            word_groups['words6'].append(x)
        if len(x) == 7 and x.isalpha():
            word_groups['words7'].append(x)
        if len(x) == 8 and x.isalpha():
            word_groups['words8'].append(x)
        if len(x) == 9 and x.isalpha():
            word_groups['words9'].append(x)
        if len(x) == 10 and x.isalpha():
            word_groups['words10'].append(x)
        if len(x) == 11 and x.isalpha():
            word_groups['words11'].append(x)
        if len(x) == 12 and x.isalpha():
            word_groups['words12'].append(x)

    return word_groups


# Generate random letters

def random_letters():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_of_random_letters = []
    for i in range(12):
        list_of_random_letters.append(alphabet[random.randint(0, 25)])
    return list_of_random_letters


# Getting word with 12 characters

def word12(dictionary,letters):
    for x in dictionary['words12']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 0 and len(x) > 2:
            return "".join(word)
def word11(dictionary,letters):
    for x in dictionary['words11']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 1 and len(x) > 2:
            return "".join(word)
def word10(dictionary,letters):
    for x in dictionary['words10']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 2 and len(x) > 2:
            return "".join(word)

def word9(dictionary,letters):
    for x in dictionary['words9']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 3 and len(x) > 2:
            return "".join(word)

def word8(dictionary,letters):
    for x in dictionary['words8']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 4 and len(x) > 2:
            return "".join(word)
def word7(dictionary,letters):
    for x in dictionary['words7']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 5 and len(x) > 2:
            return "".join(word)

def word6(dictionary,letters):
    for x in dictionary['words6']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 6 and len(x) > 2:
            return "".join(word)

def word5(dictionary,letters):
    for x in dictionary['words5']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 7 and len(x) > 2:
            return "".join(word)

def word4(dictionary,letters):
    for x in dictionary['words4']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 8 and len(x) > 2:
            return "".join(word)

def word3(dictionary,letters):
    for x in dictionary['words3']:
        word = []
        let = list(letters)
        for i in range(0, len(x)):
            if x[i] in let:
                let.remove(x[i])
                word.append(x[i])
        if len(word) == len(x) and len(let) == 9 and len(x) > 2:
            return "".join(word)