# -*- coding: utf-8 -*-
# B - Greedy Takahashi
# https://atcoder.jp/contests/abc149/tasks/abc149_b

A, B, K = map(int, input().split())

if K <= A:
    A -= K
elif K <= B:
    num = K - A
    A = 0
    B -= num
else:
    num = K - A
    A = 0
    B = B - num

print(max(A, 0), max(B, 0))

# 20:01 - 20:10（AC）
