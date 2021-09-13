import random as ran

'''names = []
for _ in range(int(input())):
    names.append(input())
'''
def fr(names):
    d = dict()
    unfNames = []
    i = 0
    while len(d) < len(names) or i < len(names):
        fr = names[i]
        names.remove(fr)
        unf = ran.choice(names)
        names.insert(i, fr)
        if unf in unfNames:
            continue
        unfNames.append(unf)
        d[fr] = unf
        i += 1

    for k, v in d.items():
        print(k, '-', v)

fr(['Светлана Зуева', 'Аркадий Белых', 'Борис Боков'])