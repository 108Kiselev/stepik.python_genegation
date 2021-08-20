'''n = int(input())
#mat = list(list(map(int, input().split())) for i in range(n))'''

def fun(n):
    mat = [['.'] * n for i in range(n)]

    for i in range(n):
        mat[i][i] = '*'
        mat[i][n-i-1] = '*'
        mat[i][n//2] = '*'
        mat[n//2][i] = '*'

    for i in mat:
        print(*i)

    


fun(5)
'''fun(3, [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])'''