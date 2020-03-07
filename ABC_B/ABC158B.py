# -*- coding: utf-8 -*-
# B - Count Balls
# https://atcoder.jp/contests/abc158/tasks/abc158_b

N, A, B = map(int, input().split())
ans = 0

if A == 0:
    ans = 0
else:
    n = N // (A + B)
    mod = N % (A + B)
    if mod > A:
        mod = A
    ans = A * n + mod

print(ans)

# 21:03 - 21:08（WA）- 21:19（WA）- 22:06（AC）
