# 求int型正整数在内存中存储时1的个数
n = int(input())
def oneCount(n):
    if n < 0:
        n = n & 0xffffffff
    bin2 = str(bin(n))[2:]
    count = 0
    for i in str(bin2):
        if i == '1':
            count += 1
    return count
print(oneCount(n))