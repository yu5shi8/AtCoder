# -*- coding: utf-8 -*-
# A - Simple Calculator
# https://atcoder.jp/contests/agc008/tasks/agc008_a

x, y = map(int, input().split())

if x <= y:
    if x >= 0 or y <= 0:
        cnt = abs(abs(x) - abs(y))
    else:
        cnt = abs(abs(x) - abs(y)) + 1
else:
    if x < 0 or y > 0:
        cnt = abs(abs(x) - abs(y)) + 2
    else:
        cnt = abs(abs(x) - abs(y)) + 1

print(cnt)

# [1] 14:09 - 15:20（WA / 解説・解答を閲覧）
# [2] 17:03 - 17:09（WA）- 17:14（WA）- 17:21（AC）
