m = int(input())
lis = []
for i in range(m):
    n = int(input())
    slis = []
    for i in range(n):
        slis.append(input())
    lis.append(slis)
res = set(lis[0])
for i in range(1, len(lis)):
    s = set(lis[i])
    res &= s

print(*sorted(res), sep='\n')