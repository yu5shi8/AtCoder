# -*- coding: utf-8 -*-
# C - Coloring Colorfully
# https://atcoder.jp/contests/abc124/tasks/abc124_c

s = input()
ans = 0

for i in range(len(s)):
    if i % 2 == int(s[i]):
        ans += 1

print(min(ans, len(s)-ans))

# 10:54 - 11:42
