n = int(input())
arr = []
res = ''
flag = False
for i in range(n):
    arr.append(int(input()))
k = int(input())
for i in range(n):
    if flag:
        break
    for j in range(n):
        if i != j:
            if arr[i] * arr[j] == k:
                res = 'ДА'
                print(res)
                flag = True
                break
else:
    res = 'НЕТ'
    print(res)