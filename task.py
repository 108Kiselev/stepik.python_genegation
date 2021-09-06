d = {}
for i in range(int(input())):
        key, *val = input().split()
        d[key] = val
l = []
for i in range(int(input())):
        x = input()
        for key, val in d.items():
                if x in val:
                        l.append(key)
print(*l, sep='\n')