# -*- coding: utf-8 -*-
# A - 閉路グラフ
# https://atcoder.jp/contests/arc030/tasks/arc030_1

from math import ceil

n = int(input())
k = int(input())
num = ceil((n - 1) / 2)

if k <= num:
    print('YES')
else:
    print('NO')

# 17:43 - 18:24（WA）- 18:29（WA）- 18:31（解説AC）
# math.ceil() は、小数点以下を切り上げしてくれる便利な関数です。
