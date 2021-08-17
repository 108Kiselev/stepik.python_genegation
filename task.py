n, m = int(input()), int(input())
mult = [[0 for i in range(m)] for j in range(n)]

for i in range(len(mult)):
    for j in range(len(mult[i])):
        mult[i][j] = i * j

for m in mult:
    print(*m)