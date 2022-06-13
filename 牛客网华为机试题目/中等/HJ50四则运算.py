while True:
    try:
        s = input().replace('{', '(').replace('[', '(').replace('}', ')').replace(']', ')')
        res = eval(s)
        print(int(res))
    except:
        break
