courses = {'CS101' : ['3004', 'Хайнс', '8:00'], 
           'CS102' : ['4501', 'Альварадо', '9:00'], 
           'CS103' : ['6755', 'Рич', '10:00'], 
           'CS101' : ['1244', 'Берк','11:00'], 
           'CS101' : ['1411', 'Ли', '13:00']}
n = input()
print(n + ': ', end='')
print(*courses.get(n), sep=', ')