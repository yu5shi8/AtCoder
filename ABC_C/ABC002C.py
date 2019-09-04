# -*- coding: utf-8 -*-
# C - 直訴
# https://atcoder.jp/contests/abc002/tasks/abc002_3

xa, ya, xb, yb, xc, yc = map(int, input().split())
calc = abs((xb-xa)*(yc-ya) - (xc-xa)*(yb-ya)) / 2
print(calc)

# 10:35 -（解説・解答を閲覧）- 11:10（AC）
