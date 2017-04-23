f = open('output.txt','w')
print('Стоимость товара: \n')
print(' Фунтов>>>')
a = int(input())
print(' Шиллингов>>>')      #  20 пенсов == 1 шиллинг
p = int(input())            #  12 шиллингов == 1 фунту    
print(' Пенсов>>>')         #  y = Пенс  ; r = Пенс
d = int(input())            #  t = шиллинг
print(a, p, d, file = f)
print('Оплачено:\n')    #Оплата товара
print(' Фунтов>>>')
q = int(input())
print(' Шиллингов>>>')
w = int(input())
print(' Пенсов>>>')
e = int(input())
print(q, w, e, file = f)
r = int(q - a)
t = int(w - p)
y = int(e - d)
while(y < 0):
    y = y + 20
    t = t - 1
while(t < 0):
    t = t + 12
    r = r - 1
while(y >= 20):
    y = y - 20
    t = t + 1
while(t >= 12):
    t = t - 12
    r = r + 1
if(r < 0):    #Если не достаточно денег
    print('Не достаточно денег')
    f.write('not enough money')
elif(r >= 0):    #Если хватает всего
    print('Ваша сдача')
    if(r > 1):
        print(r);print('^Фунтов')
    elif(r == 1):
        print(r);print('^Фунт')
    if(t > 1):
        print(t);print('^Шиллингов')
    elif(t == 1):
        print(t);print('^Шиллинг')
    if(y > 1):
        print(y);print('^Пенсов')
    elif(y == 1):
        print(y);print('^Пенс')
    print('Оплачено!')
    print('Спасибо за покупку!') #The end.
    print(r, t, y, file = f)
f.close()
