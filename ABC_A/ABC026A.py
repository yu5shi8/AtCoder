# -*- coding: utf-8 -*-
# A - 掛け算の最大値
# https://atcoder.jp/contests/abc026/tasks/abc026_a

a = int(input())
ans = 0

for x in range(a):
    y = a - x
    calc = x * y
    if x * y > ans:
        ans = x * y

print(ans)

# 16:39 - 16:42
