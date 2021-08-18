'''n = int(input())'''


def fun(n):
    mat = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                mat[i][j] = 1

    for i in mat:
        print(*i)
    
fun(4)
print()
fun(5)