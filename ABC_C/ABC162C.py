# -*- coding: utf-8 -*-
# C - Sum of gcd of Tuples (Easy)
# https://atcoder.jp/contests/abc162/tasks/abc162_c

import math

K = int(input())
check = {}
ans = 0

for i in range(201):
    check[i] = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        check[math.gcd(a, b)] += 1

for c in range(1, K+1):
    for k in check.keys():
        num = math.gcd(c, k) * check[k]
        ans += num

print(ans)

# 23:22 - 23:28（AC）
