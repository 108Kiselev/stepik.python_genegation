'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))
'''
def fun(mat, n):
    for i in range(1, n+1):
        for j in range(n):
            if i not in mat[j]:
                print('NO')
                return

    smat = [['.'] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            smat[i][j] = mat[j][i]

    for i in range(1, n+1):
        for j in range(n):
            if i not in smat[j]:
                print('NO')
                return
    print('YES')
    
    

fun([[2, 3, 4, 1],
    [3, 4, 1, 2],
    [4, 1, 2, 3],
    [1, 2, 3, 4]], 4)
print()
fun([[1, 2, 3],
    [3, 2, 1],
    [2, 3, 4]], 3)