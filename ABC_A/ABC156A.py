# -*- coding: utf-8 -*-
# A - Beginner
# https://atcoder.jp/contests/abc156/tasks/abc156_a

N, R = map(int, input().split())
under_R = 100 * (10 - N)

if N < 10:
    print(under_R + R)
else:
    print(R)

# 23:40 - 23:46（AC）
