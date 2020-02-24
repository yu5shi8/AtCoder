# -*- coding: utf-8 -*-
# C - Rally
# https://atcoder.jp/contests/abc156/tasks/abc156_c

N = int(input())
X = list(map(int, input().split()))
num = 0
ans = 10**7 + 10

for p in range(1, 101):
    for i in range(N):
        num += (X[i] - p) ** 2
    if num < ans:
        ans = num
        num = 0

print(ans)

# 19:39 - 19:54（AC）
