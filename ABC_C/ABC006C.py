# -*- coding: utf-8 -*-
# C - スフィンクスのなぞなぞ
# https://atcoder.jp/contests/abc006/tasks/abc006_3

N, M = map(int, input().split())
b = M % 2
c = (M-N*2)//2
a = N - b - c

if a >= 0 and c >= 0:
    print(a, b, c)
else:
    print(-1, -1, -1)

# [1] 9:55 - 10:03（WA / 解説を閲覧）- 10:24（WA / 解答を閲覧）- 10:40
# [2] 10:42 - 10:44（AC）
