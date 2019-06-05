# -*- coding: utf-8 -*-
# A - テスト評価
# https://atcoder.jp/contests/abc028/tasks/abc028_a

n = int(input())

if n == 100:
    print('Perfect')
elif 90 <= n <= 99:
    print('Great')
elif 60 <= n <= 89:
    print('Good')
else:
    print('Bad')

# 16:29 - 16:31
