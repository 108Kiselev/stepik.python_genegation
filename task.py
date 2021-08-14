arr = list(map(int, input().split(' ')))
dic = {}
for a in arr:
    dic[a] = 0
arr.clear()
for key in dic.keys():
    arr.append(key)
print(len(arr))