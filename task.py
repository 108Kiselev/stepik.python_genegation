n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))
j = -1

for i in range(n):
    mat[i][i], mat[j][i] = mat[j][i], mat[i][i]
    j -= 1

for i in mat:
    print(*i)