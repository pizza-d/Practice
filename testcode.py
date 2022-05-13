def match(m,d,w):
    em = [31,28,31,30,31,30,31,31,30,31,30,31]
    da = []
    w2 = w
    while w2 > 0:
        da.append(0)
        w2 -= 1
    for k in range(m,13):
        if k == m:
            for i in range(d,em[m-1]+1):
                da.append(i)
        else:
            for i in range(1,em[k-1]+1):
                da.append(i)
    da = [da[i:i+7] for i in range(0,len(da),7)]
    mi = []
    for i in da:
        if i[0] < i[-1] and i[0] != 1:
            mi.append(m)
        else:
            m += 1
            mi.append(m)
    print(mi)
    print(da)
    for k,i in enumerate(da):
        if len(i) >= w and i[w] == d:
            print(mi[k],i[w])

match(3,18,5)
