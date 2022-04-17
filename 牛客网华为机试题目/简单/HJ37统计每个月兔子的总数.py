def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def sumnum(m):
    counter = m[-1]+m[-2]
    return counter


if __name__ == '__main__':
    # a = int(input())
    # n = a-1
    # print(fib(n))
    # n = int(input()) - 1
    print(sumnum(fib(int(input()) - 1)))