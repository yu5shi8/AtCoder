# -*- coding: utf-8 -*-
# C - Forbidden List
# https://atcoder.jp/contests/abc170/tasks/abc170_c

X, N = map(int, input().split())
p = list(map(int, input().split()))
plus = minus = X
ans = X

for i in range(100):
    if ans not in p:
        print(ans)
        exit()
    plus += 1
    minus -= 1
    if minus not in p:
        print(minus)
        exit()
    elif plus not in p:
        print(plus)
        exit()

# 21:40 - 21:45（AC）
