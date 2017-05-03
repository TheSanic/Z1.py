f = open('output.txt','w')
x = ('z')
y = ('a')
for o in x:
    for i in y:
        if(((o == 'z') + (i == 'a') == 25) and ((o == -'z') + (i == -'a') == 1/6)):
            print(o, file = f)
            print(i, file = f)
f.close()
