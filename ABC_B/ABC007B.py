# -*- coding: utf-8 -*-
# B - 辞書式順序
# https://atcoder.jp/contests/abc007/tasks/abc007_2

import string

a = input()
ans = 0

if a == 'a':
    ans = -1
elif len(a) >= 2:
    num = len(a) - 1
    ans = a[0:num]
else:
    char = list(string.ascii_lowercase)
    num = char.index(a[0]) - 1
    ans = char[num]

print(ans)

# 21:53 - 22:07（AC）
