# -*- coding: utf-8 -*-
# C - Stones
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c

# WA
# 時間切れ

n = int(input())
s = input()
count = 0

if s.count('.') == n:
    print(count)
else:
    l = []
    l_count = int(s.count('#'))
    l_index = int(s.index('#'))
    for i in range(l_index, n):
        if s[i] == '#':
            l.append(i)
#    print(l)
    if l_index + len(l) == n:
        print(count)
    elif l_index > 0:
        count += n - l_index - len(l)
        print(count)
    else:
        count += n - len(l)
        print(count)
