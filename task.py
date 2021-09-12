import random as ran

num = ''
s = set()
for i in range(100):
    while len(s) < 100:
        while len(num) < 7:
            num += str(ran.randrange(10))
            if num[0] == '0':
                num = num[1:]
        s.add(int(num))
        num = ''
print(*s, sep='\n')