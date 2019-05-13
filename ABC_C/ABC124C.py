# -*- coding: utf-8 -*-
# C - Coloring Colorfully
# https://atcoder.jp/contests/abc124/tasks/abc124_c

s = input()
to_0 = 0

for i in range(len(s)):
    if i % 2 != int(s[i]):
        to_0 += 1

print(min(to_0, len(s)-to_0))

# 20:13 - 20:22
