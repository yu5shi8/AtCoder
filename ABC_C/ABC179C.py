# -*- coding: utf-8 -*-
# C - A x B + C
# https://atcoder.jp/contests/abc179/tasks/abc179_c

N = int(input())
ans = 0

for i in range(1, N+1):
    ans += (N-1) // i

print(ans)

# 21:08 - 22:40（時間切れ）
# 14:21 - 15:09（解説を閲覧）- 15:15
# 22:00 - 22:08（AC）
