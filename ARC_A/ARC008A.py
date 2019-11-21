# -*- coding: utf-8 -*-
# A - たこ焼き買えるかな？
# https://atcoder.jp/contests/arc008/tasks/arc008_1

N = int(input())
check = N % 10
mod = [7, 8, 9]

if check in mod:
    ans = 100 * (N // 10 + 1)
else:
    ans = 100 * (N // 10) + 15 * check

print(ans)

# 10:12 - 10:21（AC）
