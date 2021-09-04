s = input().lower()
signs = ['.', ',', '!', '?', ':', ';', '-']
for i in s:
        if i in signs:
                s = s.replace(i, '', 500)

res = {}
for i in s.split():
        res[i] = res.get(i, 0) + 1

d = 1000
for v in res.values():
        if v <= d:
                d = v
            
lis = sorted(res)
for i in lis:
        if res[i] == d:
                print(i)
                break