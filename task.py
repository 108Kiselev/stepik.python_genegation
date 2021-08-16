n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))

left = []
right = []

for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j:
            left.append(mat[i][j])
        elif i <= j and i >= n - 1 - j:
            right.append(mat[i][j])
print(max(max(left), max(right)))