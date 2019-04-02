# -*- coding: utf-8 -*-
# A - 居合を終え、青い絵を覆う
# https://atcoder.jp/contests/abc049/tasks/abc049_a

c = input()
aeiou = ['a', 'e', 'i', 'o', 'u']

if c[:1] in aeiou:
    print('vowel')
else:
    print('consonant')
