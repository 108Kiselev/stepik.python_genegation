'''n = int(input())
'''

def fun(n):
    mat = [['.'] * n for i in range(n)]
    mat[0][0] = 0

    for x in range(1, n+1):
        for i in range(x, n):
            mat[i-x][i] = x
            mat[i][i-x] = x
            mat[i][i] = 0  

    for i in mat:
        print(*i)
    
fun(5)
print()
fun(2)
print()
fun(3)