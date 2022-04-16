#确实没想出来咋做，复制的大佬代码看看
#但越看越觉得自己好傻逼，看起来很简单啊……
while True:
    try:
        num = int(input())
        stack = []
        for i in range(num):
            stack.append(input())
        print("\n".join(sorted(stack)))
    except:
        break
