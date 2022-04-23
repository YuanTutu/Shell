# 算法还是不会，看大佬的
while True:
    try:
        n = int(input())
        prime = []
        for i in range(int(n/2), 1,-1):
            for x in range(2,i):
                if i%x == 0 or (n-i)%x == 0:
                    break
            else:
                prime.append(i)
        print(prime[0])
        print(n-prime[0])
    except:
        break
