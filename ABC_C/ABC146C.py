# -*- coding: utf-8 -*-
# C - Buy an Integer
# https://atcoder.jp/contests/abc146/tasks/abc146_c

A, B, X = map(int, input().split())

def cost(N):
    d = len(str(N))
    calc = A * N + B * d
    return calc <= X

left = 0
right = 10**9 + 1

while left + 1 < right:
    mid = (left + right) // 2
    if cost(mid):
        left = mid
    else:
        right = mid

print(left)

# [1]（解説を閲覧）19:49 - 20:23（解答を閲覧）32m
# [2] 22:16 - 22:22（AC）
