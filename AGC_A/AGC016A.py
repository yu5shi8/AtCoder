# -*- coding: utf-8 -*-
# A - Shrinking
# https://atcoder.jp/contests/agc016/tasks/agc016_a

s = input()
ans = []

for c in s:
    ws = s.split(c)
    ans.append(max(map(len, ws)))

print(min(ans))

# 13:03 - 14:16（解説を閲覧）- 15:37（AC）
# [別解] 17:30 - 17:33（AC）
