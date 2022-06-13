while True:
    try:
        password = []
        for i in range(2):
            password.append(input())

        #加密
        for i in password[0]:
            ascii = []
            tran_ascii = []
            for j in i:
                ascii.append(ord(j))

            for j in ascii:
                # 大写变小写+1
                if 65 <= j <=89:
                    j = j + 33
                    tran_ascii.append(j)
                #Z变a
                elif j == 90:
                    j = 97
                    tran_ascii.append(j)
                #小写变大写+1
                elif 97 <= j <= 121:
                    j = j - 31
                    tran_ascii.append(j)
                #z变A
                elif j == 122:
                    j = 65
                    tran_ascii.append(j)
                #0-8替换成1-9
                elif 48 <= j <= 56:
                    j = j + 1
                    tran_ascii.append(j)
                #9变成0
                elif j == 57:
                    j = 48
                    tran_ascii.append(j)
                else:
                    pass

                for j in tran_ascii:
                    print(chr(j),end='')

        print("")
        # 解密
        for i in password[1]:
            ascii = []
            tran_ascii = []
            for j in i:
                ascii.append(ord(j))

            for j in ascii:
                # 大写变小写-1
                if 66 <= j <= 90:
                    j = j + 31
                    tran_ascii.append(j)
                #A变z
                elif j == 65:
                    j = 122
                    tran_ascii.append(j)
                #小写变大写-1
                elif 98 <= j <= 122:
                    j = j - 33
                    tran_ascii.append(j)
                #a变Z
                elif j == 97:
                    j = 90
                    tran_ascii.append(j)
                #1-9替换成0-8
                elif 49 <= j <= 57:
                    j = j - 1
                    tran_ascii.append(j)
                #0变成9
                elif j == 48:
                    j = 57
                    tran_ascii.append(j)
                else:
                    pass

                for j in tran_ascii:
                    print(chr(j),end='')



    except:
        break