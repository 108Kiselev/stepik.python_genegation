n = int(input())

mat = list(list(map(int, input().split())) for i in range(n))
m = mat[-n][-1]

#i > n - 1 - j
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if mat[i][j] > m:
                m = mat[i][j]
print(m)