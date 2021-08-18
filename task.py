'''
inp = input().split()
n = int(inp[0])
m = int(inp[1])
'''


def fun(n, m):
    mat = [[1] * m for i in range(n)]

    k = 2
    coe = 1
    for x in range(n + m - 2):
        for i in range(n):
            for j in range(m):
                if i + j == coe:
                    mat[i][j] = k
                    k += 1
        coe += 1

    for i in mat:
        print(*i)

    
fun(3, 5)
print()
fun(2, 2)