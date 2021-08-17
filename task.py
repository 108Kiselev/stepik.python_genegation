'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))'''
def fun(n, mat):
    j = -1

    for i in range(n//2):
        mat[i], mat[j] = mat[j], mat[i]
        j -= 1

    for i in mat:
        print(*i)
    
fun(4, [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [8, 6, 4, 2],
        [3, 4, 5, 6]])
print()
fun(3, [[1, 2, 3],
        [5, 6, 7],
        [8, 6, 4]])