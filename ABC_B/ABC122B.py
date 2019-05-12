# -*- coding: utf-8 -*-
# B - ATCoder
# https://atcoder.jp/contests/abc122/tasks/abc122_b

s = input()
s_0 = s[:]
s_0 = s_0.replace('A', '.').replace('G', '.').replace('C', '.').replace('T', '.')
count = 0
ans = 0

for i in range(len(s_0)):
    if s_0[i] == '.':
        count += 1
        if ans < count:
            ans = count
    else:
        count = 0

print(ans)

# 11:56 - 12:29
