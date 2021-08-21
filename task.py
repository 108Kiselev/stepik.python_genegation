'''n = int(input())
std = [input().split() for i in range(n)]
'''

def fun(n, std):
    for i in std:
        print(*i)
    print()
    for i in std:
        if i[1] == '4' or i[1] == '5':
            print(*i)

fun(5, [['Круглов', '4'],
        ['Кузнецов', '5'],
        ['Федин', '4'],
        ['Тарасов', '2'],
        ['Словецкий', '3']])