n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))

left = 0
right = 0
up = 0
down = 0

for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j:
            left += mat[i][j]
        elif i < j and i > n - 1 - j:
            right += mat[i][j]
        elif i < j and i < n - 1 - j:
            up += mat[i][j]
        elif i > j and i > n - 1 - j:
            down += mat[i][j]
print('Верхняя четверть:', up)
print('Правая четверть:', right)
print('Нижняя четверть:', down)
print('Левая четверть:', left)