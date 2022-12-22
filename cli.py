from functions import get_words, lower_case, words_split

import random


words_database = get_words()

lower_case_words = lower_case(words_database)

word_dictionary = words_split(lower_case_words)

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']


l1 = abc[random.randint(0, 25)]
l2 = abc[random.randint(0, 25)]
l3 = abc[random.randint(0, 25)]
l4 = abc[random.randint(0, 25)]
l5 = abc[random.randint(0, 25)]
l6 = abc[random.randint(0, 25)]
l7 = abc[random.randint(0, 25)]
l8 = abc[random.randint(0, 25)]
l9 = abc[random.randint(0, 25)]
l10 = abc[random.randint(0, 25)]
l11 = abc[random.randint(0, 25)]
l12 = abc[random.randint(0, 25)]

letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]


print(f"Given letters are: {letters}")


results=[]

for x in word_dictionary['words12']:
    word12 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word12.append(x[i])
    if len(word12) == len(x) and len(letters) == 0 and len(x) > 2:
        results.append(''.join(word12))
        break

for x in word_dictionary['words11']:
    word11 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word11.append(x[i])
    if len(word11) == len(x) and len(letters) == 1 and len(x) > 2:
        results.append(''.join(word11))
        break

for x in word_dictionary['words10']:
    word10 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word10.append(x[i])
    if len(word10) == len(x) and len(letters) == 2 and len(x) > 2:
        results.append(''.join(word10))
        break

for x in word_dictionary['words9']:
    word9 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word9.append(x[i])
    if len(word9) == len(x) and len(letters) == 3 and len(x) > 2:
        results.append(''.join(word9))
        break

for x in word_dictionary['words8']:
    word8 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word8.append(x[i])
    if len(word8) == len(x) and len(letters) == 4 and len(x) > 2:
        results.append(''.join(word8))
        break

for x in word_dictionary['words7']:
    word7 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word7.append(x[i])
    if len(word7) == len(x) and len(letters) == 5 and len(x) > 2:
        results.append(''.join(word7))
        break

for x in word_dictionary['words6']:
    word6 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word6.append(x[i])
    if len(word6) == len(x) and len(letters) == 6 and len(x) > 2:
        results.append(''.join(word6))
        break

for x in word_dictionary['words5']:
    word5 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word5.append(x[i])
    if len(word5) == len(x) and len(letters) == 7 and len(x) > 2:
        results.append(''.join(word5))
        break

for x in word_dictionary['words4']:
    word4 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word4.append(x[i])
    if len(word4) == len(x) and len(letters) == 8 and len(x) > 2:
        results.append(''.join(word4))
        break

for x in word_dictionary['words3']:
    word3 = []
    letters = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in letters:
            letters.remove(x[i])
            word3.append(x[i])
    if len(word3) == len(x) and len(letters) == 9 and len(x) > 2:
        results.append(''.join(word3))
        break

print(f"Longest word is: {results[0].upper()}")
