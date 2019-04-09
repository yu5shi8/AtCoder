# -*- coding: utf-8 -*-
# A - Favorite Sound
# https://atcoder.jp/contests/abc120/tasks/abc120_a

a, b, c = map(int, input().split())

if b // a >= c:
    print(c)
else:
    print(b // a)

# b // a もしくは c のうち、どちらか小さい方を答えるので
# min() を使うのがよりスマート
# print(min((b // a), c))