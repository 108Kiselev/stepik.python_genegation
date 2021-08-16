st = input()
st = st.replace(' ', '', 500) + '0'

sli = []
res = []

sli.append(st[0])

for i in range(len(st)-1):
    if st[i] == st[i+1]:
        sli.append(st[i+1])
    else:
        res.append(sli)
        sli = []
        sli.append(st[i+1])
print(res)