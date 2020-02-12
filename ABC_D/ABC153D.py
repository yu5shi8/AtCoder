# -*- coding: utf-8 -*-
# D - Caracal vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_d

H = int(input())
ans = 0

def calc(x):
    if x == 1:
        return 1
    else:
        return 2 * calc(x//2) + 1

ans = calc(H)
print(ans)

# [1] 20:56 - 23:18
# [2] 23:02 -（解説を閲覧）- 23:10（AC）
