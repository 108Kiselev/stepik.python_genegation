n = int(input())

d = {}

for i in range(n):
        s = input().split(': ')
        d[s[0].lower()] = s[1]
m = int(input())

for i in range(m):
        k = input().lower()
        print(d.get(k, 'Не найдено'))