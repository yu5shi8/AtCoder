# -*- coding: utf-8 -*-
# C - オセロ
# https://atcoder.jp/contests/abc035/tasks/abc035_c

from itertools import accumulate

N, Q = map(int, input().split())
S = [0] * (N + 1)
for i in range(Q):
    l, r = map(int, input().split())
    S[l-1] += 1
    S[r] -= 1

check = list(accumulate(S[:-1]))

ans = ''
for i in check:
    if i % 2 == 0:
        ans += '0'
    else:
        ans += '1'

print(ans)

# [1] 15:10 - 15:20（TLE）- 15:37（WA）- 15:48（TLE / 解説を閲覧）16:58
# [2] 17:36 - 17:42（AC）
