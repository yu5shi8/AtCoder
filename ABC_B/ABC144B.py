# -*- coding: utf-8 -*-
# B - 81
# https://atcoder.jp/contests/abc144/tasks/abc144_b

N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            print('Yes')
            exit()

print('No')

# 14:09 - 14:12（AC）
