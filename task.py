with open('nums.txt', encoding='utf-8') as file:
    res = 0
    for line in file.readlines():
        for i in range(len(line)):
            if not line[i].isdigit():
                line = line.replace(line[i], ' ', 1)
        res += sum(list(map(int, line.split())))

        
print(res)