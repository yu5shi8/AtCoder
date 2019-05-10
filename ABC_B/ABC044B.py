# -*- coding: utf-8 -*-
# B - 美しい文字列 / Beautiful Strings
# https://atcoder.jp/contests/abc044/tasks/abc044_b

w = input()
w = sorted(w)
set_w = list(set(w))

for i in range(len(set_w)):
    if w.count(set_w[i]) % 2 != 0:
        print('No')
        exit()
print('Yes')

# 16:39 - 16:48
