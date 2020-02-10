# -*- coding: utf-8 -*-
# A - Remaining Balls
# https://atcoder.jp/contests/abc154/tasks/abc154_a

S, T = input().split()
A, B = map(int, input().split())
U = input()

if S == U:
    A -= 1
elif T == U:
    B -= 1

print(A, B)

# 21:19 - 21:22（AC）
