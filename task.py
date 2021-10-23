names = [input() for _ in range(int(input()))]

with open('output.txt', 'w', encoding='UTF-8') as out:
    for name in names:
        with open(name, encoding='UTF-8') as inp:
            data = inp.read()
            out.write(data)