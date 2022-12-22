import random

words = open("words.txt", 'r')
word = words.read()
words = word.split('\n')

words2 = []
for x in words:
    x2 = x.lower()
    words2.append(x2)

words3 = []
words4 = []
words5 = []
words6 = []
words7 = []
words8 = []
words9 = []
words10 = []
words11 = []
words12 = []

for x in words2:
    if len(x) == 3 and x.isalpha():
        words3.append(x)
    if len(x) == 4 and x.isalpha():
        words4.append(x)
    if len(x) == 5 and x.isalpha():
        words5.append(x)
    if len(x) == 6 and x.isalpha():
        words6.append(x)
    if len(x) == 7 and x.isalpha():
        words7.append(x)
    if len(x) == 8 and x.isalpha():
        words8.append(x)
    if len(x) == 9 and x.isalpha():
        words9.append(x)
    if len(x) == 10 and x.isalpha():
        words10.append(x)
    if len(x) == 11 and x.isalpha():
        words11.append(x)
    if len(x) == 12 and x.isalpha():
        words12.append(x)

words = sorted(words, key=len)
words = words[::-1]

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

print("Ponudjena slova su:", l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12)
resenja = []
for x in words12:
    rec12 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec12.append(x[i])
    if len(rec12) == len(x) and len(slova2) == 0 and len(x) > 2:
        resenja.append(rec12)
        # print(''.join(rec12))
        break

for x in words11:
    rec11 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec11.append(x[i])
    if len(rec11) == len(x) and len(slova2) == 1 and len(x) > 2:
        resenja.append(rec11)
        # print(''.join(rec11))
        break

for x in words10:
    rec10 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec10.append(x[i])
    if len(rec10) == len(x) and len(slova2) == 2 and len(x) > 2:
        resenja.append(rec10)
        # print(''.join(rec10))
        break

for x in words9:
    rec9 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec9.append(x[i])
    if len(rec9) == len(x) and len(slova2) == 3 and len(x) > 2:
        resenja.append(rec9)
        # print(''.join(rec9))
        break

for x in words8:
    rec8 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec8.append(x[i])
    if len(rec8) == len(x) and len(slova2) == 4 and len(x) > 2:
        resenja.append(rec8)
        # print(''.join(rec8))
        break

for x in words7:
    rec7 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec7.append(x[i])
    if len(rec7) == len(x) and len(slova2) == 5 and len(x) > 2:
        resenja.append(rec7)
        # print(''.join(rec7))
        break

for x in words6:
    rec6 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec6.append(x[i])
    if len(rec6) == len(x) and len(slova2) == 6 and len(x) > 2:
        resenja.append(rec6)
        # print(''.join(rec6))
        break

for x in words5:
    rec5 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec5.append(x[i])
    if len(rec5) == len(x) and len(slova2) == 7 and len(x) > 2:
        resenja.append(rec5)
        # print(''.join(rec5))
        break

for x in words4:
    rec4 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec4.append(x[i])
    if len(rec4) == len(x) and len(slova2) == 8 and len(x) > 2:
        resenja.append(rec4)
        # print(''.join(rec4))
        break

for x in words3:
    rec3 = []
    slova2 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    for i in range(0, len(x)):
        if x[i] in slova2:
            slova2.remove(x[i])
            rec3.append(x[i])
    if len(rec3) == len(x) and len(slova2) == 9 and len(x) > 2:
        resenja.append(rec3)
        # print(''.join(rec3))
        break

print('Najduza rec je:', ''.join(resenja[0]))
