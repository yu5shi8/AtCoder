# -*- coding: utf-8 -*-
# C - Average Length
# https://atcoder.jp/contests/abc145/tasks/abc145_c

import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
p = []
cnt = 0

for v in itertools.permutations(xy, N):
    p.append(v)

for i in range(len(p)):
    for j in range(N-1):
        cnt += ((p[i][j][0] - p[i][j+1][0])**2 + (p[i][j][1] - p[i][j+1][1])**2) ** 0.5

ans = cnt / len(p)

print(ans)

# 21:05 - 21:29（AC）
