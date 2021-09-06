d = {}
for i in range(int(input())):
        key, val = input().split()
        d[key] = val
a = input()
for key, val in d.items():
        if key == a:
                print(val)
        elif val == a:
                print(key)