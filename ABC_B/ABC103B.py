# -*- coding: utf-8 -*-
# B - String Rotation
# https://atcoder.jp/contests/abc103/tasks/abc103_b

s = input()
t = input()
 
for i in range(len(s)):
    if s == t:
        print('Yes')
        break
    else:
        s_last = s[-1]
        s = s_last + s[0:len(s)-1]
if s != t:
    print('No')

# 14:59 - 15:19

# sの末尾1文字を先頭に持ってきてtと比較するということは
# sを2度繰り返し、その中にtがあるか判定することと同義
# s = input()*2
# t = input()
# if t in s:
#     print('Yes')
# else:
#     print('No')
