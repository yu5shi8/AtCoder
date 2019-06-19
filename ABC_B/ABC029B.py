# -*- coding: utf-8 -*-
# B - カキ
# https://atcoder.jp/contests/abc029/tasks/abc029_b

s = [input() for _ in range(12)]
ans = 0

for i in range(12):
    if s[i].count('r') > 0:
        ans += 1

print(ans)

# 22:40 - 22:44
