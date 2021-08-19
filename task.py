'''inp = input().split()
n = int(inp[0])
m = int(inp[1])

mat1 = [list(map(int, input().split())) for i in range(n)]
emp = input()
mat1 = [list(map(int, input().split())) for i in range(n)]'''

def fun(n, m, mat1, mat2):
    matr = [['.'] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            matr[i][j] = mat1[i][j] + mat2[i][j]
    
    for i in matr:
        print(*i)


fun(2, 4, [[1, 2, 3, 4],
            [5, 6, 7, 1]], 
           [[3, 2, 1, 2],
           [1, 3, 1, 3]])