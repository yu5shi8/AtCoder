# -*- coding: utf-8 -*-
# B - AtCoDeerくんとボール色塗り / Painting Balls with AtCoDeer
# https://atcoder.jp/contests/abc046/tasks/abc046_b

# n個のボール を k色で塗り分ける
# ただし、隣り合ったボールは同じ色に塗らない
# ボールの塗り方としてあり得るものの個数は？

n, k = map(int, input().split())
ans = k * (k-1)**(n-1)
print(ans)

# 14:55 - 16:25
# （解説を閲覧）- 16:26
