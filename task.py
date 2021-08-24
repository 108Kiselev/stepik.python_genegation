m = int(input())
n = int(input())
libr = set([input() for i in range(m)])
task = [input() for i in range(n)]
for i in task:
    print('YES' if i in libr else 'NO')