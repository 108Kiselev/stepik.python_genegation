from decimal import Decimal as decimal


with open('goats.txt', encoding='UTF-8') as goats, open('answer.txt', 'w', encoding='UTF-8') as answer:
    colors = dict()
    while 1:
        line = goats.readline().strip()
        if line == 'COLOURS': continue
        if line == 'GOATS': break
        colors[line] = 0
            
    '''for line in goats:
        line = line.strip()
        if line == 'COLOURS': continue
        if line == 'GOATS': break
        colors[line] = 0'''
    
    count = 0
    for line in goats:
        line = line.strip()
        colors[line] += 1
        count += 1
    
    res = []
    for key, value in colors.items():
        colors[key] = decimal(colors[key])/decimal(count)*100
        if colors[key] > 7: res.append(key)
    
    for i in sorted(res):
        print(i, file=answer)