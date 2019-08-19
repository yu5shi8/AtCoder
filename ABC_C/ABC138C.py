# -*- coding: utf-8 -*-
# C - Alchemist
# https://atcoder.jp/contests/abc138/tasks/abc138_c

# 小さい順にソートして合成していけば良いかな？

n = int(input())
v = list(map(int, input().split()))
v.sort()
pot = v[0]

for i in range(1, n):
    pot = (pot + v[i]) / 2

print(pot)

# 21:13 - 21:19（AC）
