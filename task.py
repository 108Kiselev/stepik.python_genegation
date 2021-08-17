'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))'''

def fun(n, mat):
    submat = [['0'] * n for i in range(n)]
    for i in range(n):
        for j in range(len(mat)):
            submat[i][j] = mat[j][i]

    for i in submat:
        for j in range(-1, -n-1, -1):
            print(i[j], end = ' ')
        print()
    
fun(4, [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [8, 6, 4, 2],
        [3, 4, 5, 6]])
print()
fun(3, [[1, 2, 3],
        [5, 6, 7],
        [8, 6, 4]])