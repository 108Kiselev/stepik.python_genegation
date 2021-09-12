import random as ran

bingo = []
s = set()
sublis = []
for i in range(5):
    while len(sublis) < 5:
        rnum = ran.randint(1, 75)
        if rnum not in s:
            sublis.append(rnum)
            s.add(rnum)
    bingo.append(sublis)
    sublis = []
bingo[2][2] = 0
for i in bingo:
    print(*i)