# -*- coding: utf-8 -*-
# C - Low Elements
# https://atcoder.jp/contests/abc152/tasks/abc152_c

N = int(input())
P = list(map(int, input().split()))

ans = 0
check = 10**9 + 7

for i in range(N):
    if check > P[i]:
        ans += 1
        check = P[i]

print(ans)

# [1] 23:34 - 23:57（TLE / 解説を閲覧）- 0:04（TLE） - 0:07（TLE）
# [2] 0:23 - 0:26（AC）
