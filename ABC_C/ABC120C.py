# -*- coding: utf-8 -*-
# C - Unification
# https://atcoder.jp/contests/abc120/tasks/abc120_c

s = list(input())
ans = 0

zero = s.count('0')
one = len(s) - zero
ans = min(zero, one) * 2

print(ans)

# 21:58 - 22:12
# 21:49 - 23:00
# 19:31 - 19:46（WA） - 19:48
