def chunked(lis , n):
    res = []
    i = 0
    m = n

    while True:
        res.append(lis[i:m])
        i += n
        m += n
        if i >= len(lis):
            break
    return res

lis = input().split()
n = int(input())

print(chunked(lis , n))