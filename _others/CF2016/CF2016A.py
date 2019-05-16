# -*- coding: utf-8 -*-
# A - Signboard
# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_a

s = input()
code = 'CODEFESTIVAL2016'
count = 0

for i in range(16):
    if s[i] != code[i]:
        count += 1

print(count)

# 19:17 - 19:29
