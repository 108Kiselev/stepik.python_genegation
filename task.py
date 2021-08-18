'''n = input()'''


def fun(n):
    mat = [[0] * n for i in range(n)]

    #j = n - i - 1 - j на побочной диаг
    for i in range(n):
        for j in range(n):
            if j == n - i - 1:
                mat[i][j] = 1
            if i > n - 1 - j:
                mat[i][j] = 2
    for i in mat:
        print(*i)
    
fun(4)
print()
fun(3)