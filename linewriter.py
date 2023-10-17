STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(arg):
    test = f'{STATICKY_TEXT}{arg}'
    with open('output.txt', 'w') as soubor:
        soubor.write(test)


    with open('output.txt', 'r') as f:
        read = f.read()
    
    return 'output.txt'

writeTextToFile(843729)

