n = int(input())

res = [0, 0, 0, 0, 0]
dot = []

def define(x, y):
    if x > 0:
        if y > 0:
            return 1
        elif y < 0:
            return 4
        else:
            return 0
    elif x < 0:
        if y > 0:
            return 2
        elif y < 0:
            return 3
        else: 
            return 0
    else:
        return 0

for i in range(n):
    dot = input().split(' ')
    for i in range(len(dot)):
        dot[i] = int(dot[i])
    out = define(dot[0], dot[1])
    res[out] += 1

print('Первая четверть:', res[1])
print('Вторая четверть:', res[2])
print('Третья четверть:', res[3])
print('Четвертая четверть:', res[4])