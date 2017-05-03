f = open('output.txt','w')
name = ('Шумахер', 'Хилл', 'Алези')
for m in name:
        if(((m != 'Шумахер') or (m == 'Хилл')) and
        ((m == 'Шумахер') or (m != 'Алези')) and
        ((m == 'Хилл') or (m == 'Алези'))):
            print(m, file = f)
            print('Занял первое место', file = f)
f.close()
