# -*- coding: utf-8 -*-
# B - Homework / 
# https://atcoder.jp/contests/abc163/tasks/abc163_b

N, M = map(int, input().split())
A = list(map(int, input().split()))

w = sum(A)
ans = N - w

if ans >= 0:
    print(ans)
else:
    print(-1)

# 22:27 - 22:30（AC）
