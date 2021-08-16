n, m = int(input()), int(input())
mat = [[input() for i in range(m)] for j in range(n)]

for i in mat:
    print(*i)

print()

for i in range(m):
    for j in range(n):
        print(mat[j][i], end = ' ')
    print()