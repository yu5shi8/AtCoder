# -*- coding: utf-8 -*-
# C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c

K = int(input())
mod = 7 % K
ans = -1

for k in range(K):
    if mod == 0:
        ans = k + 1
        break
    mod = (mod * 10 + 7) % K

print(ans)

# 14:57 - 15:09（TLE）
# （解説を閲覧）- 22:39（解答を写経）
# 20:57 - 21:09（AC）
