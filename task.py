'''n = int(input())
#std = [input().split() for i in range(n)]
'''

def fun(n):
    f1, f2, f3 = 1, 1, 1
    for i in range(n):
        print(f1, end = ' ')
        f1, f2, f3 = f2, f3, f1 + f2 + f3

fun(10)
print()
fun(1)
print()
fun(2)