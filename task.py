n, m = int(input()), int(input())
mat = list(list(map(int, input().split())) for i in range(n))

iin = 0
jin = 0
maximum = mat[0][0]

for i in range(n):
    for j in range(m):
        if mat[i][j] > maximum:
            maximum = mat[i][j]
            iin = i
            jin = j
print(iin, jin)