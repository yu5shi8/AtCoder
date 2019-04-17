# -*- coding: utf-8 -*-
# ABC086C - Traveling
# https://atcoder.jp/contests/abs/tasks/arc089_a

n = int(input())

for i in range(n):
    t, x, y = map(int, input().split())
    if (x + y) > t or (t + x + y) % 2:
        print('No')
        exit()
print('Yes')

