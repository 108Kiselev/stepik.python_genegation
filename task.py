'''n = int(input())'''


def fun(n, m):
    mat = [['a'] * m for i in range(n)]
    k = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                mat[i][j] = k
                k += 1
        else:
            for j in range(1, m+1):
                mat[i][-j] = k
                k += 1
    for i in mat:
        print(*i)

    
fun(3, 5)
print()
fun(5, 5)