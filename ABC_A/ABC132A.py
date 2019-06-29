# -*- coding: utf-8 -*-
# A - Fifty-Fifty
# https://atcoder.jp/contests/abc132/tasks/abc132_a

s = input()

if s.count(s[0]) == 4:
    print('No')
elif s[0] == s[1] and s[2] == s[3]:
    print('Yes')
elif s[0] == s[2] and s[1] == s[3]:
    print('Yes')
elif s[0] == s[3] and s[1] == s[2]:
    print('Yes')
else:
    print('No')

# 21:00 - 21:04（AC）
