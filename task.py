with open('file.txt', encoding='utf-8') as file:
    text = file.read().replace('\n', ' ', 10000)
    
    letters = 0
    for i in text:
        if i.isalpha(): letters += 1
    
    words = len(text.split())
    file.seek(0)
    lines = len(file.readlines())
    
    
    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')