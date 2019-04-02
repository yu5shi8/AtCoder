# -*- coding: utf-8 -*-
# A - One out of Three
# https://atcoder.jp/contests/abc075/tasks/abc075_a

a, b, c = map(int, input().split())

if a in (b, c):
    print(b + c - a)
elif b == c:
    print(a)
else:
    print(b)

# ^（ハット記号）を用いたXOR（右辺と左辺が異なる場合のみTrue）で書くと速い
# abc = eval(input().replace(' ', '^'))
# print(abc)
