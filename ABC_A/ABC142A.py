# -*- coding: utf-8 -*-
# A - Odds of Oddness
# https://atcoder.jp/contests/abc142/tasks/abc142_a

N = int(input())

if N % 2 != 0:
    num = N // 2 + 1
else:
    num = N // 2

ans = num / N
print('{:.06f}'.format(ans))

# 21:00 - 21:05（AC）
