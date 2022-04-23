def f(m,n):
    if n == 1 or m == 1:
        return 1
    if m < 0:
        return 0
    return f(m-n,n)+f(m,n-1)

while True:
    try:
        m,n = map(int,input().split(" "))
        print(f(m,n))
    except:
        break