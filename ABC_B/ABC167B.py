# -*- coding: utf-8 -*-
# B - Easy Linear Programming
# https://atcoder.jp/contests/abc167/tasks/abc167_b

A, B, C, K = map(int, input().split())
num = 0

if K - A <= 0:
    num = K
else:
    K -= A
    num = A
    if K - B > 0:
        K -= B
        num += (-1)*K

print(num)

# 19:41 - 20:25 - 23:43 - 21:47（AC）
