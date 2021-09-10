st = input()
dd = {}
for i in range(int(input())):
        kv = input()
        dd[kv[-1]] = kv[0]

do = {}
for i in st:
        do[i] = do.get(i, 0) + 1

res = ''
for s in st:
        res += dd[str(do[s])]
print(res)