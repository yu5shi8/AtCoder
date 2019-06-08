# -*- coding: utf-8 -*-
# B - 直方体
# https://atcoder.jp/contests/abc041/tasks/abc041_b

a, b, c = map(int, input().split())
x = a * b * c
mod = 10**9 + 7
ans = x % mod

print(ans)

# 21:10 - 21:13
