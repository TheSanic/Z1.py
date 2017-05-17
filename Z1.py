f = open('output.txt','w')
file = open('input.txt')
lest = file.read().split()
a = lest[0] ; p = lest[1] ; d = lest[2]
print(a, p, d, file = f)
q = lest[3] ; w = lest[4] ; e = lest[5]
print(q, w, e, file = f)
r = int(float(q) - float(a)) ; t = int(float(w) - float(p)) ; y = int(float(e) - float(d))
while(y < 0):
    y = y + 20 ; t = t - 1
while(t < 0):
    t = t + 12 ; r = r - 1
while(y >= 20):
    y = y - 20 ; t = t + 1
while(t >= 12):
    t = t - 12 ; r = r + 1
if(r < 0):    #Если не достаточно денег
    f.write('not enough money')
elif(r >= 0):    #Если остаётся сдача
    print(r, t, y, file = f)
f.close()
file.close()   #The end.
