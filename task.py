n = list(map(int, input().split()))
for i in range(len(n)):
    #print(set(n[0:i:]))
    if n[i] in set(n[0:i:]):
        print('YES')
    else: print('NO')