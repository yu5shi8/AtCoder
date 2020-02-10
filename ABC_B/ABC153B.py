# -*- coding: utf-8 -*-
# B - Common Raccoon vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_b

H, N = map(int, input().split())
A = sum(list(map(int, input().split())))

if H <= A:
    print('Yes')
else:
    print('No')

# 21:02 - 21:05（AC）
