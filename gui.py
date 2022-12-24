import PySimpleGUI as sg
import functions

sg.theme("LightBlue")

label1=sg.Text('Longest word game')
label2=sg.Text('Please choose letters')

let1=sg.InputText(tooltip='enter a single letter',key='l1',size=(2,2))
let2=sg.InputText(tooltip='enter a single letter',key='l2',size=(2,2))
let3=sg.InputText(tooltip='enter a single letter',key='l3',size=(2,2))
let4=sg.InputText(tooltip='enter a single letter',key='l4',size=(2,2))
let5=sg.InputText(tooltip='enter a single letter',key='l5',size=(2,2))
let6=sg.InputText(tooltip='enter a single letter',key='l6',size=(2,2))
let7=sg.InputText(tooltip='enter a single letter',key='l7',size=(2,2))
let8=sg.InputText(tooltip='enter a single letter',key='l8',size=(2,2))
let9=sg.InputText(tooltip='enter a single letter',key='l9',size=(2,2))
let10=sg.InputText(tooltip='enter a single letter',key='l10',size=(2,2))
let11=sg.InputText(tooltip='enter a single letter',key='l11',size=(2,2))
let12=sg.InputText(tooltip='enter a single letter',key='l12',size=(2,2))

button1=sg.Button('Create')
result= sg.InputText(key='word',size=(15,2))

window=sg.Window("Longest word app",
                 layout=[[label1],[label2],[let1,let2,let3,let4,let5,let6,let7,let8,let9,let10,let11,let12],[button1],
                [result]],
                 font=("Helvetica",16))

while True:

    event,value=window.read()
    print(window.read())

    match event:
        case 'Create':
            words_database = functions.get_words()
            lower_case_words = functions.lower_case(words_database)
            word_dictionary = functions.words_split(lower_case_words)
            letters=[value['l1'],value['l2'], value['l3'], value['l4'], value['l5'], value['l6'],
                     value['l7'], value['l8'], value['l9'], value['l10'],value['l11'], value['l12']]
            word12 = functions.word12(word_dictionary, letters)
            word11 = functions.word11(word_dictionary, letters)
            word10 = functions.word10(word_dictionary, letters)
            word9 = functions.word9(word_dictionary, letters)
            word8 = functions.word8(word_dictionary, letters)
            word7 = functions.word7(word_dictionary, letters)
            word6 = functions.word6(word_dictionary, letters)
            word5 = functions.word5(word_dictionary, letters)
            word4 = functions.word4(word_dictionary, letters)
            word3 = functions.word3(word_dictionary, letters)

            longestword = [word12, word11, word10, word9, word8, word7, word6, word5, word4, word3]
            result2=[]
            for x in longestword:
                if x != None:
                    result2.append(x.upper())
                    break
            window['word'].update(value=result2)

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()


