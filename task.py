'''n = int(input())'''


def fun(n, m):
    for i in range(n):
        count = 1 + i
        for j in range(m):
            print(str(count).ljust(3), end =' ')
            count += n
        print()
    
fun(3, 7)
print()
fun(6, 6)
print()
fun(7, 1)