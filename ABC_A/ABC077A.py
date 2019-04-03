# -*- coding: utf-8 -*-
# A - Rotation
# https://atcoder.jp/contests/abc077/tasks/abc077_a

c1 = input()
c2 = input()

if (c1[0] == c2[2]) and (c1[1] == c2[1]) and (c1[2] == c2[0]):
    print('YES')
else:
    print('NO')

# c2[::-1] とすると、1文字ずつ右から返してくれる
# if c1 == c2[::-1]:
#     print('YES')
# else:
#     print('NO')
