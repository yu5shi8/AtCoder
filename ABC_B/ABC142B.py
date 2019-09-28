# -*- coding: utf-8 -*-
# B - Roller Coaster
# https://atcoder.jp/contests/abc142/tasks/abc142_b

N, K = map(int, input().split())
h = list(map(int, input().split()))
ans = 0

for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)

# 21:05 - 21:07（AC）
