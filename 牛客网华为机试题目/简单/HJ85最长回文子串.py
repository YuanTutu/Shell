#单纯的判断是否为回文字还好，有个reversed()可以用用，但如果是在一串里面找，没想到思路，看看大佬们的操作，但好像都是硬算
while True:
    try:
        s = input()
        res = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # print("s[i:j] is,",s[i:j])
                # print("s[i:j][::-1] is,", s[i:j][::-1])
                if s[i:j] == s[i:j][::-1]:
                    res.append(j - i)
        if res != '':
            print(max(res))
    except:
        break
