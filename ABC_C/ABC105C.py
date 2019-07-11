# -*- coding: utf-8 -*-
# C - Base -2 Number
# https://atcoder.jp/contests/abc105/tasks/abc105_c

n = int(input())
ans = ''

if n == 0:
    print(0)
    exit()

while n != 0:
    i = n % (-2)
    n = n // (-2)
    if i < 0:
        i += 2
        n += 1
    ans += str(i)

print(ans[::-1])

# 17:09 -（解説・解答を閲覧）17:53
# （再挑戦）- 18:01（AC）
