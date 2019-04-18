# -*- coding: utf-8 -*-
# B - AcCepted
# https://atcoder.jp/contests/abc104/tasks/abc104_b

s = input()

if s[0]=='A' and s[2:-1].count('C')==1 and (s[1:s.find('C')]+s[s.find('C')+1:]).islower():
    print('AC')
else:
    print('WA')
