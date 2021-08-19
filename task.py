'''
inp = input().split()
n = int(inp[0])
m = int(inp[1])
'''


def fun(n, m):
    mat = [['.'] * m for i in range(n)]
    coe = 0
    k = 1
    fl = 0
    
    while k <= n * m:
        for i in range(coe, 1+coe):
            if fl: break
            for j in range(coe, m - coe):
                mat[i][j] = k
                if k == n * m: 
                    fl = 1
                    break
                k += 1

        for i in range(1):
            if fl: break
            for j in range(n-1-2*coe):
                mat[-n+1+coe+j][-1-coe] = k
                if k == n * m: 
                    fl = 1
                    break
                k += 1
        
        for i in range(1): #bottom
            if fl: break
            for j in range(-2-coe, -m-1+coe, -1):
                mat[-1-coe][j] = k
                if k == n * m: 
                    fl = 1
                    break
                k += 1

        for i in range(1):
            if fl: break
            for j in range(-2-coe, -n+coe, -1):
                try: mat[j][coe] = k
                except: pass
                if k == n * m: 
                    fl = 1
                    break
                k += 1
        coe += 1
        if fl or coe >= m/2: break
                
    for i in range(n):
        for j in range(m):
            print(str(mat[i][j]).ljust(3), end = ' ')
        print()

    
fun(4, 5)
print()
fun(1, 6)
print()
fun(3, 3)
print()
fun(9, 8)