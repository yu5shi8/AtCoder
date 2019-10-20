# -*- coding: utf-8 -*-
# D - Triangles
# https://atcoder.jp/contests/abc143/tasks/abc143_d

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

from bisect import bisect_left
for i in range(N):
    for j in range(i+1, N):
        ab = L[i] + L[j]
        index = bisect_left(L, ab)
        num = index - j - 1
        ans += max(0, num)

print(ans)

# 21:13 - 21:45（TLE）- 22:14（TLE）- 22:36（TLE）
