# -*- coding: utf-8 -*-
# D - Banned K
# https://atcoder.jp/contests/abc159/tasks/abc159_d

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

d = Counter(A)
total = 0

for v in d.values():
    total += (v * (v - 1)) // 2

for a in A:
    print(total - d[a] + 1)

# [1] 22:12 - 22:58（WA）- 23:05 / 23:50 - 0:00（TLE）- 0:08（TLE / 解説・解答を閲覧）
# [2] 21:52 - 22:04（AC）
