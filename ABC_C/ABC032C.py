# -*- coding: utf-8 -*-
# C - 列
# https://atcoder.jp/contests/abc032/tasks/abc032_c

N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in set(s):
    print(N)
    exit()
elif K == 0:
    print(0)
    exit()

l, r, ans = -1, 1, 0
num = 1

for r in range(0, N):
    num *= s[r]
    if num <= K:
        ans = max(ans, r-l)
    else:
        l += 1
        num //= s[l]

ans = max(ans, r-l)

print(ans)

# [1] 19:22 - 19:45（WA）/ 11:17 - 11:59（WA）/ 19:21 - 20:21（WA）
# [2] 22:04 - 22:15（AC）
