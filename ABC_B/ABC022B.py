# -*- coding: utf-8 -*-
# B - Bumble Bee
# https://atcoder.jp/contests/abc022/tasks/abc022_b

n = int(input())
a = [int(input()) for i in range(n)]

print(len(a) - len(set(a)))

# 15:16 - 15:24（TLE）- 15:29（AC）
