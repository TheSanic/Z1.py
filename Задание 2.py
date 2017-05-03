f = open('output.txt','w')
name = ('Вадим', 'Сергей', 'Михаил')
language = ('Китайский','Японский','Арабский')
for m in name:
    for l in language:
        if(((m == 'Вадим') or (l == 'Китайский')) and
        ((m == 'Сергей') or (m != 'Китайский')) and
        ((m == 'Михаил') or (m != 'Арабский'))):
            print(m, file = f)
            print('Изучает', file = f)
            print(l,'\n', file = f)
f.close()
