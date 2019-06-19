# -*- coding: utf-8 -*-
# B - 文字数カウント
# https://atcoder.jp/contests/abc028/tasks/abc028_b

s = input()
ans = [0] * 6

for i in range(len(s)):
    if s[i] == 'A':
        ans[0] += 1
    elif s[i] == 'B':
        ans[1] += 1
    elif s[i] == 'C':
        ans[2] += 1
    elif s[i] == 'D':
        ans[3] += 1
    elif s[i] == 'E':
        ans[4] += 1
    elif s[i] == 'F':
        ans[5] += 1

print(*ans, sep=' ')

# 22:28 - 22:32
