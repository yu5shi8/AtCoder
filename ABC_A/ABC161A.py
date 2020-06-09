# -*- coding: utf-8 -*-
# A - ABC Swap
# https://atcoder.jp/contests/abc161/tasks/abc161_a

X, Y, Z = map(int, input().split())

X, Y = Y, X
X, Z = Z, X

print(X, Y, Z)

# 22:22 - 22:24（AC）
