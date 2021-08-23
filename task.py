n = int(input())
lis = []
for i in range(n):
    lis.append(input().lower())
for i in lis:
    print(len(set(i)))