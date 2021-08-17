n, m = int(input()), int(input())
mat = list(list(map(int, input().split())) for i in range(n))
toCh = [int(i) for i in input().split()]

submat = [['0'] * n for i in range(m)]

for i in range(m):
    for j in range(len(mat)):
        submat[i][j] = mat[j][i]

submat[toCh[0]], submat[toCh[1]] = submat[toCh[1]], submat[toCh[0]]

for i in range(len(submat[0])):
    for j in range(len(submat)):
        print(submat[j][i], end = ' ')
    print()