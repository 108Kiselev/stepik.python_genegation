n = int(input())
mat = list(list(map(int, input().split())) for i in range(n))

for i in mat:
    srAf = sum(i) // len(i)
    count = 0
    for j in range(len(i)):
        if i[j] > srAf:
            count += 1
    print(count)