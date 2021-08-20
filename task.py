'''n = input()
'''

def fun(n):
    keys = {'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7}
    mat = [['.'] * 8 for i in range(8)]
    y = int(n[1])-1
    x = int(keys.get(n[0]))
    mat[y][x] = 'Q'
    
    for i in range(8):
        mat[i][x] = '*'
        mat[y][i] = '*'
        if x-i >= 0 and y-i >= 0: mat[y-i][x-i] = '*'
        if y+i < 8 and x+i < 8: mat[y+i][x+i] = '*'
        if x-i >= 0 and y+i < 8: mat[y+i][x-i] = '*'
        if y-i >= 0 and x+i < 8: mat[y-i][x+i] = '*'
            
    mat[y][x] = 'Q'

    for i in range(-1, -len(mat)-1, -1):
        print(*mat[i])
fun('a1')
print()
fun('c4')
print()
fun('h5')