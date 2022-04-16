while True:
    try:
        a=int(input())
        if a != 0:
            b=a/2
            print(int(b))
        elif a == 0:
            break
    except:
        break