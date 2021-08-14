tim = input()
rus = input()

if tim == rus:
    print('ничья')

dic = {'ножницы': ('бумага', 'ящерица'),
        'бумага': ('камень', 'Спок'),
        'камень': ('ножницы', 'ящерица'),
        'ящерица': ('Спок', 'бумага'),
        'Спок': ('ножницы', 'камень')}

for key, value in dic.items():
    if tim in key and rus in value:
        print('Тимур')
    else:
        if rus in key and tim in value:
            print('Руслан')