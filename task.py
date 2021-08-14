arr = list(input().split(' '))
a = arr.pop(-1)
arr.insert(0, a)
for i in arr:
    print(i, end=' ')