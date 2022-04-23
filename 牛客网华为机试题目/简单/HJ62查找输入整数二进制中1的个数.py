while True:
    try:
        a = bin(int(input()))
        # print(list(a))
        couter=0
        for i in a:
            if i == '1':
                couter+=1
        print(couter)
    except:
        break
