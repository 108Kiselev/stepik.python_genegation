'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))'''

def fun(n, mat):
    #submat = [['0'] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            print(mat[j][i], end = ' ')
        print()

    


fun(3, [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])