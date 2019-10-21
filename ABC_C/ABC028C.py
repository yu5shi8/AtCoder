# -*- coding: utf-8 -*-
# C - 数を3つ選ぶマン
# https://atcoder.jp/contests/abc028/tasks/abc028_c

from itertools import combinations

A, B, C, D, E = map(int, input().split())
L = [A, B, C, D, E]
ans = []

c = combinations(L, 3)
for v in c:
    num = sum(v)
    ans.append(num)

ans.sort()
print(ans[-3])

# 19:39 - 19:43（WA）- 19:54（AC）
