# -*- coding: utf-8 -*-
# C - String Transformation
# https://atcoder.jp/contests/abc110/tasks/abc110_c

import collections

s = list(input())
t = list(input())

c_s = collections.Counter(s)
s_values, s_counts = zip(*c_s.most_common())

c_t = collections.Counter(t)
t_values, t_counts = zip(*c_t.most_common())

if s_counts == t_counts:
    print('Yes')
else:
    print('No')

# 6:45 - 7:24（WA）- 7:31（WA）
# 19:00 - 20:16（WA）
# 21:49 - 22:05（AC）
