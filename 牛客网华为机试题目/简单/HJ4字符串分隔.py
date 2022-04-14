import re
def strSlice(str):
    if len(str)%8 != 0:
        for i in range(0,8-len(str)%8):
            str = str+'0'
        str1 = re.findall(r'.{8}',str)
        for i in str1:
            print(i)
    elif len(str)%8 == 0:
        str2 = re.findall(r'.{8}',str)
        for i in str2:
            print(i)

if __name__ == "__main__":
    keyword=input()
    strSlice(keyword)