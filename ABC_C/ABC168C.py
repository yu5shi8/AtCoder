# -*- coding: utf-8 -*-
# C - : (Colon)
# https://atcoder.jp/contests/abc168/tasks/abc168_c

import math

A, B, H, M = map(int, input().split())

h = (H/12 + (M/60)/12) * 360
m = (M/60) * 360
r = math.radians(h - m)
ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(r))

print(ans)

# [1] 15:49 - 17:01（解説を閲覧）
# [2] 19:44 - 19:53（解説を閲覧、解答を写経）
# [3] 13:55 - 14:06（AC）
