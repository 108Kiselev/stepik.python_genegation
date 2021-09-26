from functools import reduce


words = [input() for i in range(int(input()))]
words = sorted(words)
gcoe = ord('A')

def gem(st):
    return reduce(lambda su, s: su + ord(str(s).upper())-gcoe, st, 0)


print(*sorted(words, key=gem), sep='\n')