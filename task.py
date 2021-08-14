num = input()
st = ''
if len(num) == 5:
    for i in range(len(num)-1, -1, -1):
        st += num[i]
    print(int(st))
elif len(num) == 6:
    print(num[0], end='')
    for i in range(len(num)-1, 0, -1):
        st += num[i]
    print(st)
else:
    print('Длина числа не соответствует условию!')