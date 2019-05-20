# -*- coding: utf-8 -*-
# C - Dice and Coin
# https://atcoder.jp/contests/abc126/tasks/abc126_c

from fractions import Fraction

n, k = map(int, input().split())
count = [0] * n
ans = 0

for i in range(1, n+1):
    j = i
    num = k - i
    while num >= j:
        j *= 2
        count[i-1] += 1

all_pattern = [0] * n
for i in range(n):
    all_pattern[i] = Fraction(1, n*(2**count[i]))

all_pattern = sum(all_pattern)
frac_ans = Fraction(all_pattern)
ans = frac_ans.numerator / frac_ans.denominator

print('{:.12f}'.format(ans))

# 0.999986250000
# 0.999973749998

# 21:21 - 22:40（WA）
