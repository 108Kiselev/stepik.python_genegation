n = int(input())
res = []
for i in range(n):
    s = set(input())
    res.append(s)
s1 = res[0]
for i in range(1, n):
    s1 &= res[i]
print(*sorted(s1))