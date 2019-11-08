# -*- coding: utf-8 -*-
# A - ぐっすり
# https://atcoder.jp/contests/arc036/tasks/arc036_a

N, K = map(int, input().split())
T = [int(input()) for i in range(N)]

for i in range(2, N):
    if sum(T[i-2:i]) + T[i] < K:
        print(i+1)
        exit()

print(-1)

# 15:09 - 15:25（AC）
