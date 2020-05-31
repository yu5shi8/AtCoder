# -*- coding: utf-8 -*-
# C - Multiplication 3
# https://atcoder.jp/contests/abc169/tasks/abc169_c

A, B = map(str, input().split())

A = int(A)
B1, B2 = map(int, B.split('.'))
ans = (A * B1) + int(A * B2 // 100)

print(ans)


from decimal import Decimal

A, B = input().split()
ans = int(Decimal(A) * Decimal(B))
print(ans)

# 21:22 - 21:25（WA）- 21:29（WA）- 21:36（WA）
