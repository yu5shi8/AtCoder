# -*- coding: utf-8 -*-
# D - Takahashi Unevolved
# https://atcoder.jp/contests/abc180/tasks/abc180_d

X, Y, A, B = map(int, input().split())
exp = 0

while X * A <= B and X < Y:
    X *= A
    exp += 1

exp += (Y - 1 - X) // B

print(exp)

# [1] 20:23 - 21:55（時間切れ・解説を閲覧）
# [2] 22:04 - 22:09（AC）
