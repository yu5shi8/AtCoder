# -*- coding: utf-8 -*-
# A - Security
# https://atcoder.jp/contests/abc131/tasks/abc131_a

s = input()

for i in range(1, 4):
    if s[i-1] == s[i]:
        print('Bad')
        exit()

print('Good')

# 21:00 - 21:07
