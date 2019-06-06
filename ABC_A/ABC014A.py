# -*- coding: utf-8 -*-
# A - けんしょう先生のお菓子配り
# https://atcoder.jp/contests/abc014/tasks/abc014_1

a = int(input())
b = int(input())

if a % b == 0:
    ans = 0
else:
    ans = b - (a % b)

print(ans)

# 10:35 - 10:38
