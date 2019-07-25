# -*- coding: utf-8 -*-
# A - Two Integers
# https://atcoder.jp/contests/apc001/tasks/apc001_a

x, y = map(int, input().split())

if x % y == 0:
    print(-1)
else:
    i = 2
    while (x * i) % y == 0:
        i += 1
    print(x * i)

# 17:19 - 17:34（AC）
