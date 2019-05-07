# -*- coding: utf-8 -*-
# B - Picture Frame
# https://atcoder.jp/contests/abc062/tasks/abc062_b

h, w = map(int, input().split())
a = [input() for _ in range(h)]
ans = ['#'*(w+2)]

for i in range(h):
    ans.append(str('#') + str(a[i]) + str('#'))
ans.append('#'*(w+2))

for i in ans:
    print(i)

# 13:37 - 14:09
