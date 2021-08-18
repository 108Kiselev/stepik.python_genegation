'''inp = input().split()
n = int(inp[0])
m = int(inp[1])'''


def fun(n, m):
    mat = [['.'] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i % 2 == 1:
                if j % 2 != 1:
                    mat[i][j] = '*'
            else:
                if j % 2 == 1:
                    mat[i][j] = '*'
    for i in mat:
        print(*i)
    
fun(3, 4)
print()
fun(2, 2)
print()
fun(1, 8)