# -*- coding: utf-8 -*-
# B - Not Found
# https://atcoder.jp/contests/abc071/tasks/abc071_b

import string

char = string.ascii_lowercase
s = input()

for i in char:
    ans = i
    if s.count(i):
        continue
    else:
        print(ans)
        quit()
print('None')

# 13:36 - 14:32
