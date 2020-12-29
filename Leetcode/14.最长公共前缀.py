#-*- coding:utf-8 -*-

def longestCommonPrefix(strs):
    if not strs: return ""
    s1 = min(strs)
    #print(s1)
    s2 = max(strs)
    #print(s2)
    for i, x in enumerate(s1):
        print(i,x)
        if x != s2[i]:
            return s2[:i]
    return s1

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    s1 = longestCommonPrefix(strs)
    print(s1)