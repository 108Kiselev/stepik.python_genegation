n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))

def matrix(mat, n):
    flag = True
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if mat[i][j] != mat[j][i]:
                flag = False
    return flag

print('NO' if matrix(mat, n) == False else 'YES')