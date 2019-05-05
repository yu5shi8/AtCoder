# -*- coding: utf-8 -*-
# B - ss
# https://atcoder.jp/contests/abc066/tasks/abc066_b

s = input()

for i in range(len(s)//2):
    s = s[:len(s)-2]
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        exit()

# 0:25 - 0:33
