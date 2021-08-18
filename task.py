'''n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))'''

def fun(n):
    keys = {'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7}
    mat = [['.'] * 8 for i in range(9)]
    y = int(n[1])
    x = int(keys.get(n[0]))
    mat[y][x] = 'N'
    '''
    y from 1, j
    x from 0 i
    '''
    for i in range(8):
        for j in range(1, 9):
            if j == y + 2 and i == x - 1 or j == y + 2 and i == x + 1 or j == y + 1 and i == x + 2 or j == y - 1 and i == x + 2 or j == y - 2 and i == x + 1 or j == y - 2 and i == x - 1 or j == y - 1 and i == x - 2 or j == y + 1 and i == x - 2:
                mat[j][i] = '*'

    for i in range(-1, -len(mat), -1):
        print(*mat[i])
    
fun('b6')
print()
fun('f3')