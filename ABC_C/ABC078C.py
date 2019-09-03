# -*- coding: utf-8 -*-
# C - HSI
# https://atcoder.jp/contests/abc078/tasks/arc085_a

N, M = map(int, input().split())
ans = (1900*M + 100*(N-M)) * (2**M)
print(ans)

# 15:24 -（解説を閲覧）15:52 - 16:27（AC）
