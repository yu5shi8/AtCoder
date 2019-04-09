# -*- coding: utf-8 -*-
# A - Double Helix
# https://atcoder.jp/contests/abc122/tasks/abc122_a

b = input()

if b == 'A':
    print('T')
elif b == 'T':
    print('A')
elif b =='C':
    print('G')
else:
    print('C')

# 対応表を辞書で作ればスマート
# l = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
# print(l[b])