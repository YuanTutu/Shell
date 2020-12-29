#-*- coding:utf-8 -*-
def kuohao(s):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1

if __name__ == '__main__':
    s = input("输入括号：>>>")
    y = kuohao(s)
    print(y)
