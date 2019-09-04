# -*- coding: utf-8 -*-
# D - Derangement
# https://atcoder.jp/contests/abc072/tasks/arc082_b

N = int(input())
p = list(map(int, input().split()))
count = 0

for i in range(1, N):
    if i == p[i-1]:
        p[i-1], p[i] = p[i], p[i-1]
        count += 1
    if i > 1:
        if p[-1] == N:
            p[-1], p[-2] = p[-2], p[-1]
            count += 1

print(count)

# 9:44 - 10:08（AC）
