'''n = int(input())
#mat = list(list(map(int, input().split())) for i in range(n))'''

'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))
'''
def matrix(mat, n):
    #j = n - i - 1 побоч диаг
    j = 1-n
    if mat[0][0] == mat[-1][-1]:
        for i in range(n-1):
            if mat[i][n - i - 1-1] != mat[i+1][n - i - 1]: return 0
    else: return 0


    return 1

print('YES' if matrix([[0, 3, 10],
                        [4, 9, 3],
                        [7, 4, 0]], 3) else 'NO') #mat, n

print('YES' if matrix([[1, 2],
                        [3, 4]], 2) else 'NO')