# -*- coding: utf-8 -*-
# A - うるう年
# https://atcoder.jp/contests/arc002/tasks/arc002_1

Y = int(input())
ans = 'NO'

if Y % 400 == 0:
    ans = 'YES'
elif Y % 100 == 0:
    ans = 'NO'
elif Y % 4 == 0:
    ans = 'YES'

print(ans)

# 21:41 - 21:44（AC）
