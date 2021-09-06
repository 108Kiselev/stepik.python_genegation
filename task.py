d = {}
for i in range(int(input())):
        val, key = input().lower().split()
        if key in d:
                d[key] += [val]
        else: d[key] = [val]
for i in range(int(input())):
        a = input().lower()
        for key, val in d.items():
                if a == key:
                        print(*val, sep=' ')
                        break
        else: 
            print('абонент не найден')