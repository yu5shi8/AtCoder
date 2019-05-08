# -*- coding: utf-8 -*-
# B - Checkpoints
# https://atcoder.jp/contests/abc057/tasks/abc057_b

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]
ans = [0]*n

for i in range(n):
    point = 0
    for j in range(m):
        num = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])
        if j == 0:
            prev = num
            point = j + 1
        elif prev > num:
            prev = num
            point = j + 1
    ans[i] += point

print(*ans, sep='\n')

# 14:37 - 16:02
