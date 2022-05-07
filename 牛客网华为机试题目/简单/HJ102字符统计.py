# aaddccdc

while True:
    try:
        s = input()
        ss = sorted(list(set(s)), key=lambda x:s.count(x)*1000-ord(x), reverse=True)
        print("".join(ss))
    except:
        break



