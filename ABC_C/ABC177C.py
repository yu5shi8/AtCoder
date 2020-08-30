# -*- coding: utf-8 -*-
# C - Sum of product of pairs
# https://atcoder.jp/contests/abc177/tasks/abc177_c

N = int(input())
A = list(map(int, input().split()))

ans = 0
mod = 10 ** 9 + 7
num = sum(A)

for a in A:
    num -= a
    ans += a * num

print(ans % mod)

# 21:17 - 21:26（TLE）- 22:13（TLE）- 23:00（写経）
# 18:38 - 18:44（AC）
