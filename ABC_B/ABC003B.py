# -*- coding: utf-8 -*-
# B - AtCoderトランプ
# https://atcoder.jp/contests/abc003/tasks/abc003_2

s = input()
t = input()
check = ['a', 't', 'c', 'o', 'd', 'e', 'r']
count = 0

for i in range(len(s)):
    if s[i] == t[i]:
        count += 1
    elif s[i] in check and t[i] == '@':
        count += 1
    elif t[i] in check and s[i] == '@':
        count += 1
    else:
        break

if len(s) == count:
    print('You can win')
else:
    print('You will lose')

# 22:11 - 22:23（AC）
