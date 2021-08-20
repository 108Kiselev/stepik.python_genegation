st = input().split()
n = int(input())

#res = [['.'] * (len(st)//3 + 1) for i in range(n)]
res = []
subres = []
x = 0
for i in range(n):
    for j in range(x, len(st), n):
        subres.append(st[j])
    x += 1
    res.append(subres)
    subres = []
print(res)