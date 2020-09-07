# -*- coding: utf-8 -*-
# C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c
# 順列全探索で解けます。

import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

A = list(itertools.permutations(range(1, N+1)))

for a in range(len(A)):
    if A[a] == P:
        p = a
    if A[a] == Q:
        q = a

print(abs(p - q))

# 22:11 - 22:30（AC）
