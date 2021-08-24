m, n = [int(input()) for i in range(2)]
math = [input() for i in range(m)]
inf = [input() for i in range(n)]
i = 0
while len(math) != len(set(math)):
    math[i], inf[i] = inf[i], math[i]
    i += 1
math = set(math)
inf = set(inf)

res = (math - inf) | (inf - math)
print(len(res) if len(res) else 'NO')