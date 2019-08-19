# -*- coding: utf-8 -*-
# B - Resistors in Parallel
# https://atcoder.jp/contests/abc138/tasks/abc138_b

from fractions import Fraction

n = int(input())
a = list(map(int, input().split()))
num = 0

for i in range(n):
    num += Fraction(1, a[i])

bunshi = num.numerator
bunbo = num.denominator

ans = bunbo / bunshi
print('{:05f}'.format(ans))

# 21:02 - 21:13（AC）
