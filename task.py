'''n = int(input())'''


def fun(n):
    mat = [[1] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i > j and i < n - 1 - j or i < j and i > n - 1 - j:
                mat[i][j] = 0

    for i in mat:
        print(*i)
    
fun(4)
print()
fun(5)