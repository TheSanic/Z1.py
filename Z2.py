f = open('output.txt','w')
model = ('ferreri', 'pontiac', 'saab')
country = ('england', 'italian')
for m in model:
    for c in country:
        if(((m == 'ferreri') or (c == 'england')) and
        ((m == 'pontiac') or (c == 'italian')) and
        ((m == 'saab') or (c != 'england'))):
            print(m, file = f)
            print(c, file = f)
f.close()
