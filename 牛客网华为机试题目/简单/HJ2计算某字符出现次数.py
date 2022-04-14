def strCount(str1,str2):
    lowerstr=str1.lower()
    keywordstr=str2.lower()
    strlist=list(lowerstr)
    counter = 0
    for i in strlist:
        if i == keywordstr:
            counter += 1
    return counter

sentence = input()
keyword = input()
print(strCount(sentence,keyword))