s = input().split()

counter = {}
for i in s:
        if i in counter:
                print(i + '_' + str(counter[i]), end = ' ')
                counter[i] = counter.get(i, 0) + 1
        else:
                print(i, end = ' ')
                counter[i] = counter.get(i, 0) + 1