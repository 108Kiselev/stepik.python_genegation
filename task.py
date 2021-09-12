import random as r
import string as st

def generate_index():
    #st.ascii_uppercase
    #r.randrange(100)
    #AB23_56VG
    pc = r.choice(st.ascii_uppercase) + r.choice(st.ascii_uppercase) + str(r.randrange(100)) + '_' + str(r.randrange(100)) + r.choice(st.ascii_uppercase) + r.choice(st.ascii_uppercase)
    print(pc)
