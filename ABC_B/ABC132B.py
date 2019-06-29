# -*- coding: utf-8 -*-
# B - Ordinary Number
# https://atcoder.jp/contests/abc132/tasks/abc132_b

n = int(input())
p = list(map(int, input().split()))
ans = 0

for i in range(2, n):
    p1 = i - 2
    p2 = i - 1
    p3 = i
    if p[p1] <= p[p2] <= p[p3] or p[p1] >= p[p2] >= p[p3]:
        ans += 1

print(ans)

# 21:05 - 21:12（AC）
