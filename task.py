n = int(input())

origArr = []
inArr = []

for i in range(1, n+1):
    inArr.append(i)
    origArr.append(inArr)
print(*origArr, sep='\n')