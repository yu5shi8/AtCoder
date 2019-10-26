# -*- coding: utf-8 -*-
# C - 経路
# https://atcoder.jp/contests/abc034/tasks/abc034_c

from math import factorial

H, W = map(int, input().split())
mod = 1000000007

top = factorial(H + W - 2) % mod
bottom = pow((factorial(H-1)*factorial(W-1))%mod, mod-2, mod)
ans = top * bottom % mod

print(ans)

# [1] 16:58 -（解説を閲覧）17:46 - 18:09（TLE）- 18:20
# [2] 18:25 - 18:29（AC）
