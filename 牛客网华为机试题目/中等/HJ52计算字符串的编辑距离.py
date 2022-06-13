# import Levenshtein
# str1=input()
# str2=input()
# print(Levenshtein.distance(str1,str2))
# 基于动态规划的解法
def edit_dist(str1, str2):
    # m，n分别字符串str1和str2的长度
    m, n = len(str1), len(str2)

    # 构建二位数组来存储子问题（sub-problem)的答案
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # 利用动态规划算法，填充数组
    for i in range(m + 1):
        for j in range(n + 1):

            # 假设第一个字符串为空，则转换的代价为j (j次的插入)
            if i == 0:
                dp[i][j] = j

                # 同样的，假设第二个字符串为空，则转换的代价为i (i次的插入)
            elif j == 0:
                dp[i][j] = i

            # 如果最后一个字符相等，就不会产生代价
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # 如果最后一个字符不一样，则考虑多种可能性，并且选择其中最小的值
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    print(dp[m][n])
    # return dp[m][n]


str1=input()
str2=input()
edit_dist(str1,str2)