'''n = int(input())'''


def fun(n, m):
    #mat = [[0] * m for i in range(n)]
    count = 1

    for i in range(n):
        for j in range(m):
            print(str(count).ljust(3), end =' ')
            count += 1
        print()
    
fun(3, 4)
print()
fun(4, 7)
print()
fun(6, 6)