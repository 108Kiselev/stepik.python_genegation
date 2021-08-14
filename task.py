n = int(input())
count = 1
res = []

for i in range(n):
    idref = list(input())
    if 'a' in idref:
        idref = idref[idref.index('a')::]
        if 'n' in idref:
            idref = idref[idref.index('n')::]
            if 't' in idref:
                idref = idref[idref.index('t')::]
                if 'o' in idref:
                    idref = idref[idref.index('o')::]
                    if 'n' in idref:
                        idref = idref[idref.index('n')::]
                        res.append(count)
    count += 1
for r in res:
    print(r, end=' ')
'''osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton'''