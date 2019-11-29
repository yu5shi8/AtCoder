# -*- coding: utf-8 -*-
# C - 浮気調査
# https://atcoder.jp/contests/abc010/tasks/abc010_3

txa, tya, txb, tyb, T, V = map(int, input().split()) 
n = int(input())
time = T * V

for i in range(n):
    x, y = map(int, input().split())
    a = ((x-txa)**2 + (y-tya)**2) ** 0.5
    b = ((x-txb)**2 + (y-tyb)**2) ** 0.5
    if (a + b) <= time:
        print('YES')
        exit()

print('NO')

# 21:25 - 21:41（WA）- 21:42（WA）- 21:45（WA）- 21:50（WA）- 21:51（AC）
