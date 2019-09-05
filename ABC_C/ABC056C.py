# -*- coding: utf-8 -*-
# C - Go Home
# https://atcoder.jp/contests/abc056/tasks/arc070_a

X = int(input())
x = 0
t = 0

while True:
    t += 1
    x += t
    if x >= X:
        break

print(t)

# [1] 21:55 - 22:40（解説を閲覧）- （解答を閲覧）22:49
# [2] 7:58 - 8:02（AC）
