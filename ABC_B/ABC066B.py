# -*- coding: utf-8 -*-
# B - ss
# https://atcoder.jp/contests/abc066/tasks/abc066_b

s = list(input())

for i in range(1,len(s)):
    len_s = len(s) - 2 * i
    for j in range(1,len(s)):
        left = s[0:j]
        right = s[j:len_s]
        if left == right:
            ans = len(left + right)
            print(ans)
            exit()
        elif len(left) > len(right):
            break

# 22:24 - 24:13
