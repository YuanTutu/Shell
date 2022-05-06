# 这部分只是代表算法，不代表实际运算
# 当nm有一个是1的时候，那么解决方法数量就是m+n
# 当他们都大于1的时候，是一种递归情况
# if n == 1 or m == 1:
#     result[n][m] = m + n
# else:
#     result[n][m] = result[n][m-1]+result[n-1][m]
def func(x,y):

    if x == 1 or y == 1:
        return x + y
    else:
        return func(x-1, y)+func(x, y-1)

while True:
    try:
        a,b = map(int,input().split())
        c = func(a, b)
        print(c)
    except:
        break
