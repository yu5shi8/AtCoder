# -*- coding: utf-8 -*-
# A - Remaining Time
# https://atcoder.jp/contests/abc057/tasks/abc057_a

a, b = map(int, input().split())
t = a + b
if t >= 24:
    t -= 24
print(t)
