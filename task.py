'''inp = input().split()
n1 = int(inp[0])
m1 = int(inp[1])

mat1 = [list(map(int, input().split())) for i in range(n1)]
emp = input()

inp = input().split()
n2 = int(inp[0])
m2 = int(inp[1])
mat2 = [list(map(int, input().split())) for i in range(n2)]'''

def fun(n1, m1, mat1, n2, m2, mat2):
    matr = [['.'] * n1 for i in range(n1)]
    sum = 0

    for i in range(n1):
        for j in range(m2):
            for x in range(m1):
                sum += mat1[i][x] * mat2[x][j]
            matr[i][j] = sum
            sum = 0

                

    for i in matr:
        print(*i)

fun(3, 3, [[2, 4, 6],
           [1, 3, 5],
           [0, 4, 8]], 
    3, 3, [[6, 3, 1],
           [9, 6, 3],
           [0, 2, 0]])