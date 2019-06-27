# -*- coding: utf-8 -*-
# C - Candles
# https://atcoder.jp/contests/abc107/tasks/arc101_a

n, k = map(int, input().split())
x = sorted(list(map(int, input().split())) + [0])
ans = 10**9 + 10

for i in range(n-k+1):
    left = i
    right = i+k
    to_right = abs(x[left]) + abs(x[right]-x[left])
    to_left = abs(x[right]) + abs(x[right]-x[left])
    if min(to_right, to_left) < ans:
        ans = min(to_right, to_left)

print(ans)

# 15:45 - 17:03（解説を見てAC）
