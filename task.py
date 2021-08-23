n = int(input())
lis = ''
for i in range(n):
    lis += input().lower()
print(len(set(lis)))