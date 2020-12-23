# class Solution:
#     def reverse(self, x: int) -> int:

def fanzhuan(x):
    if abs(x) < 2147483647:
        str_x = str(x)
        if str_x[0] != "-":
            x = int(str_x[::-1])
        else:
            x = int(str_x[:0:-1])
            x = -x
        if abs(x) < 2147483647:
            return x
        else:
            return 0
    else:
        return 0

if __name__ == '__main__':
    x = int(input(">>>"))
    y = fanzhuan(x)
    print(y)