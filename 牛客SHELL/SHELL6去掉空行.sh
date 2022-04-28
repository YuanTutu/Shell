#!/bin/bash

awk '/[^$]/ {print $1}' nowcoder.txt

# awk '/pattern/ {action}' filenames
# 正则部分（参考讨论中ArlRa大佬的解释）：
#     ^$联合使用，中间不加任何字符数字，代表匹配空行；
#     [ ] 在shell正则中表示取反
#     [^$] 在shell正则中则代表非空

# action部分：
#     {print $n}
#     $n 当前记录的第n个字段，字段间由FS分隔,默认以tab键或者空格为分隔符将一行分为多个字段