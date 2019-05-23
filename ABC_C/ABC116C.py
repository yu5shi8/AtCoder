# -*- coding: utf-8 -*-
# C - Grand Garden
# https://atcoder.jp/contests/abc116/tasks/abc116_c

n = int(input())
h = list(map(int, input().split()))
ans = h[0]

for i in range(1, n):
    if h[i] > h[i-1]:
        ans += h[i] - h[i-1]

print(ans)

# 10:15 - 10:18
