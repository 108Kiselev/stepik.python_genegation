acts = {'write': 'W',
        'read': 'R',
        'execute': 'X'}

files = {}

for n in range(int(input())):
    i = input().split()
    files[i[0]] = i[1:]

for m in range(int(input())):
    i = input().split()
    print('OK' if acts.get(i[0]) in files.get(i[1]) else 'Access denied')