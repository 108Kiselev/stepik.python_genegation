arr = list(input().split(' '))
end = ''
if len(arr) % 2 != 0:
    end = arr.pop()
for i in range(0, len(arr)-1, 2):
    #print(arr[i], arr[i+1])
    arr[i], arr[i+1] = arr[i+1], arr[i]
for a in arr:
    print(a, end = ' ')
if end.isdigit():
    print(end)