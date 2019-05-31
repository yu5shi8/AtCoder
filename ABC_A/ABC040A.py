# -*- coding: utf-8 -*-
# A - 赤赤赤赤青
# https://atcoder.jp/contests/abc040/tasks/abc040_a

n, x = map(int, input().split())

if n // 2 >= x:
    print(x - 1)
else:
    print(n - x)

# 22:40 - 22:46
