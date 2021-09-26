from random import choice


with open('first_names.txt', encoding='utf-8') as fn, open('last_names.txt', encoding='utf-8') as ln:
    fnames = [line.strip() for line in fn.readlines()]
    lnames = [line.strip() for line in ln.readlines()]
    
    for _ in range(3):
        print(f'{choice(fnames)} {choice(lnames)}')