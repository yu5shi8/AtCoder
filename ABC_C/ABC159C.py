# -*- coding: utf-8 -*-
# C - Maximum Volume
# https://atcoder.jp/contests/abc159/tasks/abc159_c

from decimal import Decimal

L = int(input())

w = Decimal(L / 3)
d = Decimal(L / 3)
h = Decimal(L / 3)

ans = Decimal(w * d * h)

print(ans)

# 22:15 - 22:19（AC）
