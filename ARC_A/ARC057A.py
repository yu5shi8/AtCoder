# -*- coding: utf-8 -*-
# A - 2兆円
# https://atcoder.jp/contests/arc057/tasks/arc057_a

A, K = map(int, input().split())
t = A
i = 0

if K == 0:
    print(2*10**12 - A)
    exit()

while t < 2*10**12:
    i += 1
    d = 1 + K*t
    ans = d + t
    t = ans

print(i)

# 19:57 - 20:15 / 13:44 - 13:47（AC）
