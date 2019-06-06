# -*- coding: utf-8 -*-
# A - 世界のFizzBuzz
# https://atcoder.jp/contests/abc006/tasks/abc006_1

n = input()

if n.count('3') > 0 or int(n) % 3 == 0:
    print('YES')
else:
    print('NO')

# 11:03 - 11:07
