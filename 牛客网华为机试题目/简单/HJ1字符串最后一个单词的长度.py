def findLen(str):
    word=str.split()
    return len(word[-1])
sentence = input()
print(findLen(sentence))