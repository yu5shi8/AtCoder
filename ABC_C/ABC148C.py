# -*- coding: utf-8 -*-
# C - Snack
# https://atcoder.jp/contests/abc148/tasks/abc148_c

import fractions

A, B = map(int, input().split())

ans = A * B // fractions.gcd(A, B)

print(ans)

# 21:08 - 21:11（AC）
