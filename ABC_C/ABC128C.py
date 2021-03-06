# -*- coding: utf-8 -*-
# C - Switches
# https://atcoder.jp/contests/abc128/tasks/abc128_c

n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0

for i in range(2**n):
    light = 0
    for j in range(m):
        count = 0
        for k in range(1, ks[j][0]+1):
            if i & 2**(ks[j][k]-1) == 2**(ks[j][k]-1):
                count += 1
        if count % 2 == p[j]:
            light += 1
    if light == m:
        ans += 1

print(ans)

# 15:38 - 18:06
