# -*- coding: utf-8 -*-
# B - Crane and Turtle
# https://atcoder.jp/contests/abc170/tasks/abc170_b

X, Y = map(int, input().split())

for i in range(X+1):
    if Y - i*2 == 4*(X-i):
        print('Yes')
        exit()

print('No')

# [1] 21:03 - 21:10（WA）- 21:15（WA）- 21:34（WA）- 21:38（WA）- 21:55（WA）- 21:58（WA）- 22:30（WA）
# [2] 11:07 - 11:10（AC）
