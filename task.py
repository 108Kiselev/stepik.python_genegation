n = input().lower()
m = input().lower()
s = ['.', ',', '!', '?', ':', ';', '-', ' ']

for i in n:
        if i in s:
                n = n.replace(i, '', 500)
for i in m:
        if i in s:
                m = m.replace(i, '', 500)

nn = {}
mm = {}

for i in n:
        nn[i] = nn.get(i, 0) + 1

for i in m:
        mm[i] = mm.get(i, 0) + 1
print("YES" if nn == mm else "NO")