# -*- coding: utf-8 -*-
# A - 9x9
# https://atcoder.jp/contests/abc144/tasks/abc144_a

A, B = map(int, input().split())

if A < 10 and B < 10:
    print(A * B)
else:
    print(-1)

# 21:00 - 21:01（AC）
