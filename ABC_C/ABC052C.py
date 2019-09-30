# -*- coding: utf-8 -*-
# C - Factors of Factorial
# https://atcoder.jp/contests/abc052/tasks/arc067_a

N = int(input())
mod = 10**9 + 7

pf = {}
for i in range(2, N+1):
    for j in range(2, int(i**0.5)+1):
        while i % j == 0:
            pf[j] = pf.get(j, 0) + 1
            i //= j
    if i > 1:
        pf[i] = pf.get(i, 0) + 1

ans = 1
for p in pf.values():
    ans = ans * (p+1) % mod

print(ans)

# [1] 17:07 - 17:58（解説を閲覧）-（解答を閲覧）18:49
# [2] 19:41 - 19:54（解答を閲覧）
# [3] 20:06 - 20:14（AC）
