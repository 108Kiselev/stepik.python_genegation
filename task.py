'''
n = int(input())
mator = [list(map(int, input().split())) for i in range(n)]
m = int(input())
'''

def mXm(n, mat1, mat2, cou, m):
    matr = [['.'] * n for i in range(n)]
    sum = 0

    for i in range(n):
        for j in range(n):
            for x in range(n):
                sum += mat1[i][x] * mat2[x][j]
            matr[i][j] = sum
            sum = 0
    cou += 1
    if cou == m: 
        for i in matr:
            print(*i)
        return 
    mXm(n, matr, mat2, cou, m)


mXm(3, [[1, 2, 1],
        [3, 3, 3],
        [1, 2, 1]], 
    [[1, 2, 1],
    [3, 3, 3],
    [1, 2, 1]], 1, 5)

'''for i in res:
    print(*i)'''