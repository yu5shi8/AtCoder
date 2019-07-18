# -*- coding: utf-8 -*-
# B - 入浴時間
# https://atcoder.jp/contests/abc012/tasks/abc012_2

n = int(input())

hour = n // 3600
minute = n // 60 % 60
second = n % 60

# print(str('{:02}'.format(hour)) + ':' + str('{:02}'.format(minute)) + ':' + str('{:02}'.format(second)))
print('{:02d}:{:02d}:{:02d}'.format(hour, minute, second))

# 17:46 - 17:53（WA）- 17:59（AC）
