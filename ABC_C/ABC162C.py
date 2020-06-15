# -*- coding: utf-8 -*-
# C - Sum of gcd of Tuples (Easy)
# https://atcoder.jp/contests/abc162/tasks/abc162_c

import math

K = int(input())
ans = 0

A = {}
for a in range(1, K+1):
    A[a] = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        num = math.gcd(a, b)
        A[num] += 1

for c in range(1, K+1):
    for k in A.keys():
        num = math.gcd(c, k) * A[k]
        ans += num

print(ans)

# 22:14 - 22:47（?）
# 10:52 - 11:05（AC）
