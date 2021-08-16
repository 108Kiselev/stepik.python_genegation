n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))

sum = 0

for i in range(len(mat)):
    sum += mat[i][i]
print(sum)