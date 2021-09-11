d = dict()
for _ in range(int(input())):
    i = input().split()
    if i[0] in d:
        if i[1] in d[i[0]]:
            d[i[0]][i[1]] += int(i[2])
        else: d[i[0]][i[1]] = int(i[2])
    else: d[i[0]] = {i[1]: int(i[2])}
sub = sorted(d)
for s in sub:
    print(s + ':')
    sortedGoods = sorted(d[s])
    for i in sortedGoods:
        print(i + ' ' + str(d[s][i]))