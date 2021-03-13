# -*- coding: utf-8 -*-
# B - Blocks on Grid
# https://atcoder.jp/contests/abc186/tasks/abc186_b

H, W = map(int, input().split())
A = []
num = 101
ans = 0

for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)
    if min(a) < num:
        num = min(a)

for h in range(H):
    for w in range(W):
        ans += A[h][w] - num

print(ans)

# 13:53 - 14:00（AC）
