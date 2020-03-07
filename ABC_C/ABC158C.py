# -*- coding: utf-8 -*-
# C - Tax Increase
# https://atcoder.jp/contests/abc158/tasks/abc158_c

A, B = map(int, input().split())

for i in range(1, 1100):
    ai = int(i * 0.08)
    bi = int(i * 0.1)
    if ai == A and bi == B:
        print(i)
        exit()

print(-1)

# [1] 21:13 - 22:29（WA）- 22:34（WA）
# [2] 0:03 - 0:11（AC）
