st = input()
count = 0
for i in range(len(st)):
    count += 0.6
    count = round(count, 2)
print(int(count), "р. ", end='')
print(int(count * 100 % 100), "коп.")