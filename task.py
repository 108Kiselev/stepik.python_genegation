'''n = int(input())'''


def fun(n, m):
    subm = []
    k = 1
    for i in range(m):
        subm.append(k)
        k += 1
    print(*subm)

    for i in range(n-1):
        subm.insert(m, subm.pop(0))
        print(*subm)

    
fun(5, 5)
print()
fun(3, 7)