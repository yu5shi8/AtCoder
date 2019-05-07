# -*- coding: utf-8 -*-
# B - Varied
# https://atcoder.jp/contests/abc063/tasks/abc063_b

s = input()
s = sorted(s)

for i in range(len(s)):
    prev = i - 1
    if s[prev] == s[i]:
        print('no')
        break
else:
    print('yes')

# 13:21 - 13:34
