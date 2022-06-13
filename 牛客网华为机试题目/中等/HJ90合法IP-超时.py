while True:
    try:
        IPADDR = list(map(int,input().split('.')))
        if len(IPADDR) == 4:
            a=0
            for i in IPADDR:
               if not i.isdigit():
                   print("NO")
               elif int(i) > 255 or (i.startswith('0') and len(i) > 1):  # 最大值大于255 或者数字为'03'这种格式的，NO
                   print("NO")
               else:
                   a+=1
            if a == 4:
                print("YES")
        else:
            print("NO")
    except:
        print("NO")