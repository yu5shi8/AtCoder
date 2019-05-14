# -*- coding: utf-8 -*-
# B - K-th Common Divisor
# https://atcoder.jp/contests/abc120/tasks/abc120_b

a, b, k = map(int, input().split())
l = []

for i in range(max(a, b)+1, 0, -1):
    if a % i == 0 and b % i == 0:
        l.append(i)

print(l[k-1])

# 21:46 - 21:56
