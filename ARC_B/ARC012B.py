# -*- coding: utf-8 -*-
# B - アキレスと亀
# https://atcoder.jp/contests/arc012/tasks/arc012_2

N, va, vb, L = map(int, input().split())

for i in range(N):
    L /= va
    L *= vb

ans = '{:.7f}'.format(L)
print(ans)

# 15:40 - 15:53（WA）- 16:00（AC）
