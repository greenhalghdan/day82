from INTAlphabet import alphabet

def converttext(input_text):
    split = list(input_text)
    newword= ''
    for letter in split:
        if newword != '':
            newword += ' '
        newletter = alphabet[letter]
        newword += newletter

    return newword



input_text = input('enter the text would you like to convert: ')
output = converttext(input_text.lower())
print(output)