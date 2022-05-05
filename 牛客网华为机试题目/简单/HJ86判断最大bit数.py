# 万万没想到啊，切片啊，何必非要硬算呢……

while True:
    try:
        a = int(input())
        b = str(bin(a)[2:])
        c = b.split('0')
        l = []
        for i in c:
            l.append(len(i))
        print(max(l))
    except:
        break
