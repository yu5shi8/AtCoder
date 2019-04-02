# -*- coding: utf-8 -*-
# A - September 9
# https://atcoder.jp/contests/abc073/tasks/abc073_a

n = input()
if n[0] == '9' or n[1] == '9':
    print('Yes')
else:
    print('No')

# if n[0] == '9' or n[1] == '9':
# ↓ スマートにできる
# if '9' in n:
