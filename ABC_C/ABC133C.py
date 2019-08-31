# -*- coding: utf-8 -*-
# C - Remainder Minimization 2019
# https://atcoder.jp/contests/abc133/tasks/abc133_c

L, R = map(int, input().split())
mod = 2019
ans = 10 ** 9 * 10

for l in range(L, min(L + mod, R) + 1):
    for r in range(l + 1, min(L + mod, R) + 1):
        ans = min(ans, (l * r) % mod)

print(ans)

# [1] 12:50 - 13:08（TLE・解説・解答を閲覧）- 13:32
# [2] 17:42 - 17:45（WA）- 17:48（AC）
