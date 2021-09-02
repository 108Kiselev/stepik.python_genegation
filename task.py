but = {1: ['.', ',', '?', '!', ':'],
            2: 	['a', 'b', 'c'],
            3: 	['d', 'e', 'f'],
            4: 	['g', 'h', 'i'],
            5: 	['j', 'k', 'l'],
            6: 	['m', 'n', 'o'],
            7: 	['p', 'q', 'r', 's'],
            8: 	['t', 'u', 'v'],
            9: 	['w', 'x', 'y', 'z'],
            0: 	' '}

st = input().lower()

for i in st:
    for k, v in but.items():
        if i in v:
            print(str(k)*int(v.index(i)+1), end = '')