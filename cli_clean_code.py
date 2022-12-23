from functions import get_words,lower_case,words_split,random_letters,word12,word11,word10,word9,word8,word7,word6, word5,word4,word3


words_database = get_words()

lower_case_words = lower_case(words_database)

word_dictionary = words_split(lower_case_words)



letters = list(random_letters())
print(f"Givven letters are {letters}")


word12= word12(word_dictionary,letters)
word11= word11(word_dictionary,letters)
word10= word10(word_dictionary,letters)
word9= word9(word_dictionary,letters)
word8= word8(word_dictionary,letters)
word7= word7(word_dictionary,letters)
word6= word6(word_dictionary,letters)
word5= word5(word_dictionary,letters)
word4= word4(word_dictionary,letters)
word3= word3(word_dictionary,letters)

longestword=[word12,word11,word10,word9,word8,word7,word6,word5,word4,word3]
for x in longestword:
    if x != None:
        print(f"Longest word is : {x.upper()}")
        break




