# -*- coding: utf-8 -*-
# A - Traveling Budget
# https://atcoder.jp/contests/abc092/tasks/abc092_a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a >= b and c >= d:
    print(b + d)
elif a >= b and  c < d:
    print(b + c)
elif a < b and c >= d:
    print(a + d)
else:
    print(a + c)

# min() で比較するとスマートになります
# if min(a, b) and min(c, d):
#     print(min(a, b) + min(c, d))