# -*- coding: utf-8 -*-
# C - Multiple Clocks
# https://atcoder.jp/contests/abc070/tasks/abc070_c

import fractions
from functools import reduce

def lcm_base(A, B):
    return (A * B) // fractions.gcd(A, B)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())
T = [int(input()) for _ in range(N)]

print(lcm(T))

# 17:33 - 17:50（AC）
