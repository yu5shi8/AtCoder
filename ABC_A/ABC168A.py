# -*- coding: utf-8 -*-
# A - ∴ (Therefore)
# https://atcoder.jp/contests/abc168/tasks/abc168_a

N = input()

if N[-1] == '3':
    print('bon')
elif N[-1] in ['0', '1', '6', '8']:
    print('pon')
else:
    print('hon')

# 17:28 - 17:31（AC）
