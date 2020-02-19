# -*- coding: utf-8 -*-
# B - Achieve the Goal
# https://atcoder.jp/contests/abc151/tasks/abc151_b

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
ans = -1

A = sum(A)
NM = N * M
x = NM - A

if x < 0:
    ans = 0
elif 0 <= x <= K:
    ans = x

print(ans)

# 22:28 - 22:41（AC）
