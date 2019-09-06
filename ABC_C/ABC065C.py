# -*- coding: utf-8 -*-
# C - Reconciled?
# https://atcoder.jp/contests/abc065/tasks/arc076_a

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
    exit()

import math

mod = 10**9 + 7

if N == M:
    ans = ((math.factorial(N) * math.factorial(M)) * 2) % mod
else:
    ans = (math.factorial(N) * math.factorial(M)) % mod

print(ans)

# [1] 13:55 - 14:49（何の方針も立たず）- 休憩 -（解説を閲覧）14:59 - 15:13（PyPyでTLE）-（解答を閲覧）- 15:21（AC）
# [2] 15:36 - 15:40（AC）
