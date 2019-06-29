# -*- coding: utf-8 -*-
# C - Modulo Summation
# https://atcoder.jp/contests/abc103/tasks/abc103_c

import fractions
from functools import reduce

n = int(input())
a = list(map(int, input().split()))
ans = 0

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

num = lcm(*a) - 1

for i in range(n):
    ans += num % a[i]

print(ans)

# 15:14 - 15:41（AC）
