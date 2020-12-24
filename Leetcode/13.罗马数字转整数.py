#-*- coding:utf-8 -*-
def zhuan(roma):
    dic_roma={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    str_x = str(roma)
    str_y = 0
    print("len(str_x):", len(str_x))
    for i in range(len(str_x)):
        print("i:",i)
        print("dic_roma_str_x[{}]:".format(i),dic_roma[str_x[i]])
        if i < len(str_x) - 1 and dic_roma[str_x[i]] < dic_roma[str_x[i + 1]]:
            str_y -= dic_roma[str_x[i]]
        else:
            str_y += dic_roma[str_x[i]]
    return str_y
if __name__ == "__main__":
    roma=input("罗马数字:>>>")
    num=zhuan(roma)
    print(num)
