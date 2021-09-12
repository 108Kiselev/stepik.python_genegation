import random

length = int(input())
st = ''

for i in range(65, 91):
    st += chr(i)
for i in range(97, 123):
    st += chr(i)

pas = ''
for _ in range(length):
    i = random.randint(0, len(st))
    pas += st[i]
 
print(pas)