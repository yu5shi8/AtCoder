# -*- coding: utf-8 -*-
# B - N重丸
# https://atcoder.jp/contests/abc026/tasks/abc026_b

import math

n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse = True)
width = 0

for i in range(n):
    if i % 2 == 0:
        width += r[i] ** 2
    else:
        width -= r[i] ** 2

ans = width * math.pi

print(ans)

# 14:18 - 14:29（AC）
