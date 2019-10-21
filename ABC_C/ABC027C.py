# -*- coding: utf-8 -*-
# C - 倍々ゲーム
# https://atcoder.jp/contests/abc027/tasks/abc027_c

N = int(input())
win = False

for i in range(2):
    x = 1
    t = True
    while x <= N:
        x *= 2
        if t ^ i == 0:
            x += 1
        t = not t
    win = win or t

print(['Aoki', 'Takahashi'][win])

# [1] 18:22 - 18:52（WA）- 18:55（WA / 解説・解答を閲覧）- 19:09
# [2] 19:16 - 19:28（AC）
