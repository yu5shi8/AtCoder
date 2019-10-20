# -*- coding: utf-8 -*-
# B - TAKOYAKI FESTIVAL 2019
# https://atcoder.jp/contests/abc143/tasks/abc143_b

N = int(input())
d = list(map(int, input().split()))
ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        ans += d[i] * d[j]

print(ans)

# 21:02 - 21:08（AC）
