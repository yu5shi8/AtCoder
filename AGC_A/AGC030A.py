# -*- coding: utf-8 -*-
# A - Poisonous Cookies
# https://atcoder.jp/contests/agc030/tasks/agc030_a

a, b, c = map(int, input().split())

if c <= a + b:
    ans = b + c
else:
    ans = a + b*2 + 1

print(ans)

# 11:05 - 11:53
