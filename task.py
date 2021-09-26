def read_csv():
    with open('data.csv', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        res = []
        for line in file:
            values = line.strip().split(',')
            res.append({k: v for k, v in zip(keys, values)})
        

        print(*res, sep='\n\n')


read_csv()