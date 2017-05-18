file = open('output.txt','w')
fil = open('input.txt','r')
e = 0
while e <= 2016:
    s = fil.read()
    z = s[0:3]
    x = s[3:10]
    charlist = []
    for q in x:
        charlist.append(q)
    print(charlist)
    charlist.reverse()
    print(charlist)
    c = (charlist[0] + charlist[1] + charlist[2] + charlist[3] + charlist[4] + charlist[5] + charlist[6])
    v = (c + z)     #Шифр(1)
    charlist.clear()
    print(v)
    b = v[0:7]
    n = v[7:10]
    for q in n:
        charlist.append(q)
    print(charlist)
    charlist.reverse()
    m = (charlist[0] + charlist[1] + charlist[2])
    a = (m + b)     #Шифр(3,7)
    print(a)
    i = a[0:6]
    o = a[6:10]
    charlist.clear()
    for q in o:
        charlist.append(q)
    print(charlist)
    charlist.reverse()
    p = (charlist[0] + charlist[1] + charlist[2] + charlist[3])
    u = (p + i)     #Шифр(3,7,6)
    print(u)
    ii = u[0:5]
    oo = u[5:10]
    charlist.clear()
    for q in oo:
        charlist.append(q)
    print(charlist)
    charlist.reverse()
    pp = (charlist[0] + charlist[1] + charlist[2] + charlist[3] + charlist[4])
    uu = (pp + ii)     #Шифр(3,7,6,5)
    print(uu)
    iii = uu[0:2]
    ooo = uu[2:10]
    charlist.clear()
    for q in ooo:
        charlist.append(q)
    print(charlist)
    charlist.reverse()
    ppp = (charlist[0] + charlist[1] + charlist[2] + charlist[3] + charlist[4] + charlist[5] + charlist[6] + charlist[7])
    uuu = (ppp + iii)
    fil = open('input.txt','w')
    w = uuu
    print(w, file = fil)
    fil.close()
    e = (e + 1)
    charlist.clear()
file.close
fil.close()
