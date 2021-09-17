import random as ran
import string as st

#n - count
#m - length

def gen(n, m):
    baseUp = set(st.ascii_uppercase) - set('IO')
    baseLow = set(st.ascii_lowercase) - set('lo')
    baseDig = set(st.digits) - set('10')
    base = baseUp | baseLow | baseDig
    
    for _ in range(n):
        pas = p = ''
        p += ran.choice(list(baseUp))
        p += ran.choice(list(baseLow))
        p += str(ran.choice(list(baseDig)))
        pas += p
        while len(pas) < m:
            pas += ran.choice(list(base))
        print(pas)

gen(3, 6)