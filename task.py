from datetime import datetime
from decimal import Decimal as decimal


def isMoreHour(item):
    start = list(map(int, item[1].split(':')))
    end = list(map(int, item[2].split(':')))
    d1 = datetime(2021, 9, 7, start[0], start[1])
    d2 = datetime(2021, 9, 7, end[0], end[1])
    delta = decimal((d2 - d1).seconds)/decimal(3600)
    return 1 if delta >= 1 else 0

with open('logfile.txt', encoding='UTF-8') as log, open('output.txt', 'w', encoding='UTF-8') as out:
    data = [line.strip().split(', ') for line in log.readlines()]
    data = filter(isMoreHour, data)
    for d in data:
        print(d[0])