'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))'''

def fun(n, mat):
    flag = 0
    for i in range(1, n**2 + 1):
        for j in mat:
            if i in j:
                flag = 1
        if not flag: 
            print('NO')
            return
        flag = 0

    summ = sum(mat[0])

    for i in mat:
        if summ != sum(i):
            print('NO')
            return

    for i in range(n):
        subsumm = 0
        for j in range(n):
            subsumm += mat[j][i]
        if subsumm != summ:
            print('NO')
            return

    summd = 0
    for i in range(n):
        summd += mat[i][i]
    if summd != summ:
        print('NO')
        return
    
    summd = 0
    for i in range(n):
        summd += mat[i-n][i]
    if summd != summ:
        print('NO')
        return
    print('YES')
    
fun(3, [[8, 2, 6,],
        [3, 5, 7,],
        [4, 9, 1]])
print()
fun(3, [[0, 1, 6,],
        [3, 5, 7,],
        [4, 9, 2]])
