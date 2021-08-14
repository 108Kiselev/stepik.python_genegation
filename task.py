num = input()
count = 0
arr = []
if len(num) < 4:
    print(num)
else:
    for i in num:
        arr.append(i)
    for i in range(len(arr), 0, -1):
        if count == 3:
            arr.insert(i, ',')
            count = 0
        count += 1
for i in arr:
    print(i, end='')