# -*- coding: utf-8 -*-
# A - Getting Difference
# https://atcoder.jp/contests/agc018/tasks/agc018_a

import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

N, K = map(int, input().split())
A = list(map(int, input().split()))

G = gcd(*A)
M = max(A)

if K % G == 0 and M >= K:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

# 16:03 - 16:23（TLE）- 17:03（TEL / 解説を閲覧）- 17:14（AC）
