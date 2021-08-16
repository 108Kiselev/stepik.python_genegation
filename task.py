lis = input().split()

res = [[]]

for i in lis:
    res.append(list(i))

i = 0
j = 2
count = 1

while j <= len(lis):
    while j <= len(lis):
        res.append(lis[i:j])
        i += 1
        j += 1
    i = 0
    j = 2 + count
    count += 1
print(res)