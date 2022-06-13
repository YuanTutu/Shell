while True:
    try:
        list = input().split()
        n=list[0]
        word=list[1:-2]
        x=list[-2]
        k=list[-1]
        # print(n,word,x,k)

        # num = 0
        broword=[]

        for i in word:
            if i == x:
                continue
            elif sorted(i) == sorted(x):
                # num+=1
                broword.append(i)
        # print(num)

        newbroword=sorted(broword)
        print(len(newbroword))
        print(newbroword[int(k)-1])
    except:
        break