# -*- coding: utf-8 -*-
# B - One Clue
# https://atcoder.jp/contests/abc137/tasks/abc137_b

k, x = map(int, input().split())

min_num = x - k + 1
max_num = x + k
array = []

for i in range(min_num, max_num):
    array.append(i)

print(*array, sep=' ')

# 21:03 - 21:06（AC）
