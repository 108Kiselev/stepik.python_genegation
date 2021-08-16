n, m = int(input()), int(input())
mat = [[input() for i in range(m)] for j in range(n)]

for i in mat:
    print(*i)