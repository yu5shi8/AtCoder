# -*- coding: utf-8 -*-
# C - Distinct or Not
# https://atcoder.jp/contests/abc154/tasks/abc154_c

N = int(input())
A = list(map(int, input().split()))

A = set(A)

if N == len(A):
    print('YES')
else:
    print('NO')

# 23:15 - 23:16（AC）
