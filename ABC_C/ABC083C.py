# -*- coding: utf-8 -*-
# C - Multiple Gift
# https://atcoder.jp/contests/abc083/tasks/arc088_a

X, Y = map(int, input().split())
x = X
ans = 0

while x <= Y:
    x *= 2
    ans += 1

print(ans)

# [1] 21:55 -（解説・解答を閲覧）-（写経）22:44
# [2] 10:10 - 10:11（AC）
