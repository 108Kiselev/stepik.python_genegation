s = input().split()

counter = {}
for i in s:
        if i in counter:
                print(counter[i]+1, end = ' ')
                counter[i] = counter.get(i, 0) + 1
        else:
                print(1, end = ' ')
                counter[i] = 1