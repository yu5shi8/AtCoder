# -*- coding: utf-8 -*-
# B - ATCoder
# https://atcoder.jp/contests/abc122/tasks/abc122_b

s = input()
k = ['A', 'G', 'C', 'T']
i = 0

while i < len(s):
    if s[i] in k:
        s = s
    else:
        s_changed = s[:i] + 'z' + s[i + 1:]
        s = s_changed
    i += 1

s_split = s.split('z')
ans = len(max(s_split, key=len))
print(ans)
