with open('population.txt', encoding='utf-8') as file:
    coun = [line.strip().split('\t') for line in file.readlines()]
    coun = filter(lambda c: 1 if c[0][0] == 'G' and int(c[1]) > 500000 else 0, coun)
    for i in coun:
        print(i[0])