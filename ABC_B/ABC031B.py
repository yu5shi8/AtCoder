# -*- coding: utf-8 -*-
# B - 運動管理
# https://atcoder.jp/contests/abc031/tasks/abc031_b

l, h = map(int, input().split())
n = int(input())
a = [int(input()) for i in range(n)]

for i in range(n):
    if l <= a[i] <= h:
        print(0)
    elif a[i] < l:
        print(l - a[i])
    else:
        print(-1)

# 21:38 - 22:07（AC）
