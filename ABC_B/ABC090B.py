# -*- coding: utf-8 -*-
# B - Palindromic Numbers
# https://atcoder.jp/contests/abc090/tasks/abc090_b

a, b = map(int, input().split())
count = 0

for i in range(a, b+1):
    if str(i)[0]==str(i)[4] and str(i)[1]==str(i)[3]:
        count += 1

print(count)

# 6:16 - 6:36
