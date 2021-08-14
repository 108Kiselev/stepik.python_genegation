n = int(input())
k = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i)
i = 0
while len(arr) > 1:
     i = (i+(k)-1)%(len(arr))
     arr.remove(arr[i])
print(arr[0])